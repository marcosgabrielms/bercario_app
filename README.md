# Sistema de Gerenciamento de Berçário

### Acesso à Aplicação

**Acesse a aplicação em funcionamento no link abaixo:**

[**bercario-app-production.up.railway.app**](https://bercarioapp-production.up.railway.app/)

---

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

Um sistema web simples para o gerenciamento de cadastros em um berçário. A aplicação permite registrar médicos, responsáveis e bebês de forma organizada e interativa.

## ✨ Funcionalidades

-   **Cadastro de Médicos:** Adiciona novos médicos ao sistema com nome, especialidade e CRM.
-   **Cadastro de Responsáveis:** Registra pais ou responsáveis com informações de contato.
-   **Cadastro de Bebês:** Permite cadastrar bebês, associando-os a um médico e a um responsável já existentes no banco de dados.
-   **Interface de Página Única (SPA):** Navegação fluida e instantânea entre os formulários, sem a necessidade de recarregar a página, graças à manipulação do DOM com JavaScript.

## 🛠️ Arquitetura e Tecnologias

Este projeto foi desenvolvido com uma arquitetura moderna que separa as responsabilidades entre o frontend, o backend e o banco de dados.

### **Banco de Dados**

-   O modelo de dados relacional foi projetado e visualizado utilizando o **MySQL Workbench**.
-   O banco de dados MySQL está hospedado na nuvem através da plataforma **Railway**, garantindo que a aplicação possa ser acessada de qualquer lugar.

### **Backend**

-   Desenvolvido em **Python** com o microframework **Flask**.
-   Serve a aplicação principal e expõe uma API RESTful simples com endpoints (`/api/medicos`, `/api/responsaveis`) que retornam dados em formato JSON para o frontend.

### **Frontend**

-   Construído como uma **Single-Page Application (SPA)**.
-   Utiliza **HTML**, **CSS** e **JavaScript** puro (vanilla JS).
-   A lógica de interface, como a exibição e ocultação de formulários, é controlada dinamicamente através da **manipulação do DOM**.
-   Os dados para os formulários dinâmicos (como a lista de médicos no cadastro de bebês) são consumidos da API do backend de forma assíncrona com `fetch`.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação em seu ambiente local.

### **Pré-requisitos**

-   Python 3.x
-   Pip (gerenciador de pacotes do Python)

### **Instalação**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/marcosgabrielms/bercario_app.git](https://github.com/marcosgabrielms/bercario_app.git)
    cd bercario_app
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    (Certifique-se de que seu arquivo `requirements.txt` contém o seguinte)
    ```txt
    Flask
    mysql-connector-python
    gunicorn
    ```
    (Depois, execute o comando de instalação)
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o Banco de Dados:**
    As credenciais de conexão com o banco de dados do Railway já estão no arquivo `app.py`. Certifique-se de que elas estão corretas.

5.  **Rode a aplicação:**
    ```bash
    python app.py
    ```

6.  Acesse `http://127.0.0.1:5000` em seu navegador.

---
