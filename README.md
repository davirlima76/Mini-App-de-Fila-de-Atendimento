# 🏥 Sistema de Gerenciamento de Fila de Atendimento

Aplicação web desenvolvida em **Python + Flask + SQLite** para gerenciamento de uma fila de atendimento.

O sistema permite cadastrar clientes, visualizar a fila de espera, chamar o próximo cliente seguindo a ordem de chegada (**FIFO**), alterar o status do atendimento e cancelar atendimentos.

---

## 📌 Sobre o Projeto

O projeto foi desenvolvido com o objetivo de aplicar conceitos de desenvolvimento web utilizando **Python**, o framework **Flask** e o banco de dados **SQLite**.

A aplicação simula o funcionamento de uma fila de atendimento, onde os clientes são atendidos seguindo a ordem em que foram cadastrados.

### 🔄 Funcionamento

```text
Cadastrar cliente
       ↓
Entra na fila
       ↓
Status: Aguardando
       ↓
Chamar próximo
       ↓
Status: Em atendimento
       ↓
Concluir
       ↓
Status: Concluído
```

Caso seja necessário interromper o atendimento, o cliente também pode ser **cancelado**.

---

## ⚙️ Funcionalidades

* ✅ Cadastrar cliente na fila
* ✅ Visualizar clientes cadastrados
* ✅ Organizar a fila por ordem de chegada
* ✅ Chamar o próximo cliente
* ✅ Utilizar lógica FIFO
* ✅ Alterar status do atendimento
* ✅ Concluir atendimento
* ✅ Cancelar atendimento
* ✅ Armazenar os dados utilizando SQLite

---

## 🧠 Conceito FIFO

O sistema utiliza o conceito **FIFO (First In, First Out)**.

Isso significa:

> O primeiro cliente que entra na fila é o primeiro cliente a ser atendido.

### Exemplo

```text
Fila:

1. João
2. Maria
3. Carlos
4. Ana
```

Ao clicar em **Chamar Próximo**, João será chamado primeiro.

Depois:

```text
João    → Em atendimento
Maria   → Aguardando
Carlos  → Aguardando
Ana     → Aguardando
```

Quando João for concluído, Maria será a próxima.

---

## 🛠️ Tecnologias utilizadas

### Backend

* **Python**
* **Flask**

### Banco de dados

* **SQLite**

### Frontend

* **HTML5**
* **CSS3**
* **Jinja2**

---

## 📁 Estrutura do Projeto

```text
fila-atendimento/
│
├── app.py
│
├── fila.db
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

### 📄 `app.py`

Arquivo principal da aplicação.

Responsável por:

* iniciar o Flask;
* conectar ao banco;
* criar a tabela;
* cadastrar clientes;
* consultar a fila;
* chamar o próximo cliente;
* concluir atendimentos;
* cancelar atendimentos.

### 📄 `index.html`

Interface principal do sistema.

É responsável por apresentar:

* formulário de cadastro;
* botão para chamar o próximo;
* lista de clientes;
* status dos atendimentos;
* ações disponíveis.

### 📄 `style.css`

Arquivo responsável pela aparência da aplicação.

### 📄 `fila.db`

Banco de dados SQLite utilizado para armazenar os clientes e seus respectivos atendimentos.

> O arquivo pode ser criado automaticamente na primeira execução do sistema.

---

## 🗄️ Banco de Dados

A aplicação utiliza uma tabela chamada `clientes`.

### Estrutura

| Campo          | Tipo     | Descrição               |
| -------------- | -------- | ----------------------- |
| `id`           | INTEGER  | Identificador único     |
| `nome`         | TEXT     | Nome do cliente         |
| `status`       | TEXT     | Situação do atendimento |
| `data_entrada` | DATETIME | Data e hora de entrada  |

### Status disponíveis

```text
Aguardando
Em atendimento
Concluído
Cancelado
```

---

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Depois entre na pasta:

```bash
cd fila-atendimento
```

---

### 2. Instalar o Flask

No terminal:

```bash
py -m pip install flask
```

---

### 3. Executar a aplicação

```bash
py app.py
```

O Flask disponibilizará a aplicação em:

```text
http://127.0.0.1:5000
```

Abra esse endereço no navegador.

---

## 🧪 Testando o sistema

Para testar o funcionamento:

1. Cadastre um cliente.
2. Cadastre mais alguns clientes.
3. Observe a ordem de chegada.
4. Clique em **Chamar próximo**.
5. Verifique se o primeiro cliente mudou para **Em atendimento**.
6. Clique em **Concluir**.
7. Chame o próximo cliente.
8. Teste também o botão **Cancelar**.

### Exemplo

```text
Cliente        Status

João           Concluído
Maria          Em atendimento
Carlos         Aguardando
Ana            Aguardando
```

---

## 🔐 Regras do sistema

1. Todo novo cliente entra com o status **Aguardando**.
2. O próximo cliente é escolhido pela ordem de chegada.
3. Clientes concluídos não retornam para a fila.
4. Clientes cancelados não são chamados novamente.
5. Apenas clientes com status **Aguardando** podem ser chamados pelo botão **Chamar próximo**.
6. O histórico permanece armazenado no banco de dados.

---

## 📚 Objetivos de aprendizagem

Este projeto permite praticar:

* Desenvolvimento web com Python;
* Criação de rotas com Flask;
* Requisições HTTP;
* Formulários HTML;
* Templates Jinja2;
* Operações CRUD;
* SQL;
* Banco de dados SQLite;
* Organização de projetos web;
* Lógica de filas;
* Conceito FIFO.

---

## 👨‍💻 Desenvolvimento

Projeto desenvolvido como atividade prática para aplicação dos conhecimentos de **Python, Flask, SQLite, HTML e CSS**.

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.
