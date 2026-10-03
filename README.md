# Zelda API

![Python Version](https://img.shields.io/badge/python-3.14%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136.1-009688?logo=fastapi)
![Build Status](https://img.shields.io/github/actions/workflow/status/carine-neris/zelda-api/deploy.yml?branch=main)

Uma API que lista jogos da franquia The Legend of Zelda, construída utilizando Python e FastAPI.

## 🚀 Sobre o Projeto

O **Zelda API** é um serviço backend que fornece informações sobre os jogos e personagens da famosa franquia The Legend of Zelda. A aplicação foi desenvolvida focando em performance, simplicidade e boas práticas.

**Tecnologias Principais:**
- **FastAPI**: Framework web moderno e rápido.
- **SQLAlchemy**: ORM (Object Relational Mapper) para interação com o banco de dados.
- **Uvicorn**: Servidor ASGI leve e de alta performance.
- **Poetry**: Gerenciador moderno de dependências e empacotamento.
- **Pytest**: Framework para criação e execução de testes automatizados.

---

## 📂 Arquitetura do Projeto

A base de código está organizada da seguinte maneira:

```text
zelda-api/
├── .github/workflows/   # Fluxos de CI/CD (GitHub Actions)
├── config/              # Configurações globais (ex: conexão com o banco de dados)
├── modules/             # Funcionalidades separadas por domínio (ex: games, characters)
│   ├── games/
│   └── characters/
├── tests/               # Suíte de testes automatizados e de arquitetura
├── main.py              # Ponto de entrada da aplicação FastAPI
├── pyproject.toml       # Gerenciamento de dependências e metadados via Poetry
└── .pre-commit-config.yaml # Configuração de hooks para padronização de código
```

---

## 📋 Pré-requisitos

Para rodar este projeto localmente, você precisará ter instalado em sua máquina:

- [Python 3.14+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- Git

---

## 🛠️ Passo a Passo para Desenvolvimento Local

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd zelda-api
   ```

2. **Instale as dependências com o Poetry:**
   ```bash
   poetry install
   ```

3. **Configure o Pre-Commit:**
   O projeto utiliza `pre-commit` para garantir formatação e linting automático antes de cada commit.
   ```bash
   poetry run pre-commit install
   ```

4. **Banco de Dados (SQLite):**
   Para facilitar o desenvolvimento, a aplicação utiliza **SQLite**. As tabelas necessárias e o arquivo local `zelda.db` são **criados automaticamente** pela aplicação na sua primeira inicialização.

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   poetry run uvicorn main:app --reload
   ```

6. **Acesse a API e as Documentações Interativas:**
   - Base URL: `http://localhost:8000`
   - Swagger UI: `http://localhost:8000/docs` (Recomendado para testar endpoints)
   - ReDoc: `http://localhost:8000/redoc`

---

## 🔌 Exemplos de Uso

Uma vez que a aplicação esteja rodando, você pode utilizar o próprio Swagger em `/docs` ou ferramentas como `curl` e Postman.

**Buscar Jogos**
```bash
curl -X 'GET' 'http://localhost:8000/games/' -H 'accept: application/json'
```

---

## 🧪 Como Rodar os Testes

A suíte de testes utiliza o `pytest` e inclui testes unitários, de integração e validações de arquitetura (via `pytest-archon`). Para executá-los:

```bash
poetry run pytest
```

---

## ☁️ Como Fazer o Deploy (Implantação)

O projeto possui CI/CD configurado utilizando **GitHub Actions** para realizar o deploy automatizado para a **Azure**.

1. O fluxo de deploy (`deploy.yml`) é acionado automaticamente em todo `push` para a branch `main`.
2. **Processo do Workflow:**
   - Configura o Python e instala o Poetry.
   - Executa toda a suíte de testes em um ambiente isolado.
   - Em caso de sucesso nos testes, empacota o código junto com o `requirements.txt`.
   - Executa o deploy no Azure Web App (aplicação `zelda`).
3. **Requisitos Exigidos na Azure:**
   Para o deploy funcionar, é necessário configurar a chave secreta `AZURE_WEBAPP_PUBLISH_PROFILE` em `Settings > Secrets and variables > Actions` no seu repositório GitHub.

---

## 🤝 Como Contribuir

1. Faça um Fork do projeto.
2. Crie uma branch para a sua feature (`git checkout -b feature/minha-feature`).
3. Faça os commits das suas alterações (lembre-se que o `pre-commit` irá validar seu código).
4. Envie a sua branch (`git push origin feature/minha-feature`).
5. Abra um Pull Request explicando suas melhorias.
