Sistema de Cadastro e Consulta

Aplicação web desenvolvida em Python com Flask para cadastro, listagem e busca de registros em banco de dados SQLite.

Descrição
    Projeto criado para demonstrar domínio dos fundamentos de desenvolvimento backend, incluindo:
    Estruturação de aplicação Flask
    Persistência de dados com SQLite
    Validação de dados no fluxo de cadastro
    Integração entre front-end e back-end
    Organização de código e escopo bem definido
    O sistema pode ser facilmente adaptado para diferentes tipos de cadastros, como leads, clientes, produtos ou fornecedores.

Tecnologias Utilizadas
    Python
    Flask
    SQLite
    HTML
    CSS

Funcionalidades
    Cadastro de registros com validação de campos obrigatórios
    Validação de formato de e-mail
    Listagem ordenada por data de cadastro
    Busca por nome, e-mail ou empresa
    Banco de dados criado automaticamente na inicialização da aplicação

Execução do Projeto
pip install -r requirements.txt
python app.py

A aplicação estará disponível em http://localhost:5001.

Escopo e Decisões Técnicas
    Este projeto possui escopo intencionalmente controlado, sem:
    Autenticação ou controle de acesso
    Exclusão ou edição de registros
    Integrações externas
    Dashboard ou visualizações gráficas
    O foco é evidenciar clareza arquitetural, lógica de negócio simples e boas práticas em projetos backend de pequeno porte.
    Objetivo do Projeto

Demonstrar capacidade de:
    Modelar dados simples
    Implementar operações CRUD básicas (Create e Read)
    Organizar um projeto Python de forma clara
    Resolver necessidades reais de negócio com soluções enxutas

Licença

Uso livre para fins educacionais ou comerciais.