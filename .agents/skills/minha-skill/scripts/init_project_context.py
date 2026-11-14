#!/usr/bin/env python3
"""Initialize and inspect a versionable project-context memory with Git-aware caching."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

SKIP_DIRS = {
    ".git", "node_modules", "dist", "build", "coverage", ".next", ".nuxt",
    "target", "vendor", "__pycache__", ".venv", ".tox", "out",
}
FILES = [
    "00-index.md",
    "01-system-map.md",
    "02-runtime-and-dataflow.md",
    "03-domain-glossary.md",
    "04-conventions-and-decisions.md",
    "05-open-questions.md",
    "06-task-notes.md",
]
CACHE_FILE = ".cache.json"
LOCK_FILES = {"package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lockb"}
MANIFEST_NAMES = {
    "package.json", "pyproject.toml", "requirements.txt", "go.mod", "Cargo.toml",
    "pom.xml", "build.gradle", "composer.json", "Gemfile", "mix.exs", "pubspec.yaml",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def run_git(root: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args],
            check=True, capture_output=True, text=True,
        )
        return result.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def git_info(root: Path) -> dict[str, str | None]:
    return {
        "root": run_git(root, "rev-parse", "--show-toplevel"),
        "sha": run_git(root, "rev-parse", "HEAD"),
        "branch": run_git(root, "branch", "--show-current") or "detached",
    }


def inventory(root: Path) -> dict[str, object]:
    files: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        rel = path.relative_to(root)
        if rel.parts and (rel.parts[0].startswith(".") or rel.name in LOCK_FILES):
            continue
        files.append(rel.as_posix())
    manifests = [p for p in files if Path(p).name in MANIFEST_NAMES]
    return {"root": str(root), "file_count": len(files), "manifests": manifests, "sample_files": files[:120]}


def filesystem_digest(root: Path, files: list[str]) -> str:
    digest = hashlib.sha256()
    for name in files:
        path = root / name
        try:
            digest.update(name.encode())
            digest.update(path.read_bytes())
        except OSError:
            digest.update(f"missing:{name}".encode())
    return digest.hexdigest()


def changed_files(root: Path, previous_sha: str | None, current_sha: str | None) -> list[str]:
    changed: set[str] = set()
    if previous_sha and current_sha and previous_sha != current_sha:
        output = run_git(root, "diff", "--name-only", f"{previous_sha}..{current_sha}", "--") or ""
        changed.update(line for line in output.splitlines() if line)
    staged = run_git(root, "diff", "--name-only", "--cached", "--") or ""
    unstaged = run_git(root, "diff", "--name-only", "--") or ""
    untracked = run_git(root, "ls-files", "--others", "--exclude-standard") or ""
    for output in (staged, unstaged, untracked):
        changed.update(line for line in output.splitlines() if line)
    # A memória é o resultado do scan, não uma entrada que deve disparar outro scan.
    changed = {name for name in changed if name != ".project-context" and not name.startswith(".project-context/")}
    return sorted(changed)


def load_cache(context: Path) -> dict[str, object] | None:
    target = context / CACHE_FILE
    try:
        return json.loads(target.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def save_cache(context: Path, payload: dict[str, object]) -> None:
    target = context / CACHE_FILE
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def scaffold(root: Path, context: Path, force: bool) -> dict[str, object]:
    context.mkdir(exist_ok=True)
    data = inventory(root)
    for name in FILES:
        target = context / name
        if target.exists() and not force:
            continue
        title = name.removesuffix(".md")[3:].replace("-", " ").title()
        target.write_text(
            f"# {title}\n\n"
            "> Memória do projeto. Atualize com fatos verificáveis, evidências e confiança.\n\n"
            "## Notas\n\n"
            "### [A preencher | confiança: baixa]\n"
            "- Evidência: ainda não analisada\n"
            "- Entendimento: \n"
            f"- Atualizado em: {now()[:10]}\n",
            encoding="utf-8",
        )
    index = context / "00-index.md"
    if not index.exists() or force:
        index.write_text(
            "# Project Context Index\n\n"
            "> Gerado pelo `init_project_context.py`; confirme e refine após explorar o projeto.\n\n"
            f"- Arquivos visíveis no inventário: **{data['file_count']}**\n"
            f"- Manifestos detectados: {', '.join(data['manifests']) or 'nenhum'}\n"
            "- Stack: a confirmar\n"
            "- Entrypoints: a confirmar\n"
            "- Comandos de validação: a confirmar\n"
            "- Cache: consulte `.cache.json` ou execute `--status`\n\n"
            "## Capítulos\n\n"
            + "\n".join(f"- [{name}]({name})" for name in FILES[1:])
            + "\n\n## Inventário inicial\n\n"
            + "\n".join(f"- `{item}`" for item in data["sample_files"])
            + "\n",
            encoding="utf-8",
        )
    return data


def status(root: Path, context: Path, force_refresh: bool = False) -> dict[str, object]:
    cache = load_cache(context) or {}
    info = git_info(root)
    current_inventory = inventory(root)
    previous_sha = cache.get("last_scan_sha") if isinstance(cache.get("last_scan_sha"), str) else None
    current_sha = info["sha"]
    changes = changed_files(root, previous_sha, current_sha)
    dirty = bool(changes)
    if force_refresh or not cache.get("last_scan_at"):
        action = "full-scan"
        reason = "refresh solicitado" if force_refresh else "nenhum cache concluído"
    elif not dirty and previous_sha == current_sha:
        action = "cache-hit"
        reason = "SHA e working tree não mudaram"
    else:
        action = "delta-scan"
        reason = "há commits novos ou alterações locais"
    return {
        "action": action,
        "reason": reason,
        "project": str(root),
        "git_sha": current_sha,
        "branch": info["branch"],
        "previous_scan_sha": previous_sha,
        "last_scan_at": cache.get("last_scan_at"),
        "mode": cache.get("mode", "key-files"),
        "changed_files": changes,
        "inventory": current_inventory,
    }


def mark_complete(root: Path, context: Path, mode: str) -> dict[str, object]:
    info = git_info(root)
    files = inventory(root)["sample_files"]
    payload = {
        "schema": "web-project-mentor.context-cache.v2",
        "last_scan_at": now(),
        "last_scan_sha": info["sha"],
        "last_scan_branch": info["branch"],
        "mode": mode,
        "working_tree_digest": filesystem_digest(root, files),
        "memory_files": FILES,
    }
    save_cache(context, payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize and inspect project-context cache")
    parser.add_argument("--project", default=".", help="Project root")
    parser.add_argument("--force", action="store_true", help="Overwrite scaffold files only")
    parser.add_argument("--status", action="store_true", help="Print cache status and changed files")
    parser.add_argument("--refresh", action="store_true", help="Force a full-scan recommendation")
    parser.add_argument("--mark-complete", action="store_true", help="Record that the current analysis is complete")
    parser.add_argument("--mode", choices=("key-files", "read-all"), default="key-files")
    args = parser.parse_args()
    root = Path(args.project).resolve()
    context = root / ".project-context"
    data = scaffold(root, context, args.force)
    if args.mark_complete:
        result = {"action": "marked-complete", "cache": mark_complete(root, context, args.mode)}
    elif args.status or args.refresh:
        result = status(root, context, args.refresh)
    else:
        result = {"action": "initialized", "context_dir": str(context), "inventory": data}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
