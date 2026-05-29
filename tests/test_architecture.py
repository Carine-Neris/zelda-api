from pytest_archon import archrule

def test_clean_architecture_automatic_rules():
    # 1. Garante que as camadas de domínio não importem a infraestrutura
    archrule("Domain não conhece Infra") \
        .match("*.domain*") \
        .should_not_import("*.infrastructure*") \
        .check("modules")

    # 2. Garante que as camadas de aplicação não conheçam a camada Web (HTTP/Router)
    archrule("Application não conhece Web") \
        .match("*.application*") \
        .should_not_import("*.infrastructure.web*") \
        .check("modules")

    # 3. Garante o isolamento entre os módulos de jogos e personagens
    archrule("Games isolado de Characters") \
        .match("modules.games*") \
        .should_not_import("modules.characters*") \
        .check("modules")

    archrule("Characters isolado de Games") \
        .match("modules.characters*") \
        .should_not_import("modules.games*") \
        .check("modules")
        
    # 5. Garante que use cases do mesmo módulo não se acoplem/importem entre si
    archrule("Use cases devem ser isolados") \
        .match("modules.*.application.use_cases.*") \
        .should_not_import("modules.*.application.use_cases.*") \
        .check("modules")