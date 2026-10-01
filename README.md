# 📦 Sistema de Gestão de Estoque (CRUD)

Um sistema de gerenciamento de produtos via terminal (CLI) desenvolvido em Python e SQLite. O projeto realiza operações de CRUD (Create, Read, Update, Delete) diretamente em um banco de dados relacional, com tratamento de exceções para garantir a integridade das entradas do usuário.

## 🚀 Tecnologias Utilizadas
- **Python 3:** Lógica estruturada, laços de repetição, funções modulares e tratamento de erros (`try/except`).
- **SQLite3:** Banco de dados relacional nativo (DDL e DML).
- **Git & GitHub:** Versionamento de código e histórico estruturado de commits.
- **Linux (Terminal):** Ambiente de desenvolvimento e execução.

## ⚙️ Funcionalidades
- **Cadastro de produtos:** Proteção rigorosa contra entradas inválidas, impedindo quebra do sistema caso o usuário digite texto em campos numéricos.
- **Listagem formatada:** Visualização limpa dos itens cadastrados com conversão e formatação de valores monetários.
- **Persistência de dados:** Integração direta com arquivo `.db`, garantindo que os registros sobrevivam ao fechamento do programa.
- **Menu interativo:** Navegação contínua operando sob um loop `while True`.

## 🛠️ Como rodar o projeto na sua máquina
1. Clone este repositório:
   ```bash
   git clone [https://github.com/AndersonG-Dev/meu-primeiro-app.git](https://github.com/AndersonG-Dev/meu-primeiro-app.git)