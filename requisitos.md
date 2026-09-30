# 📋 Requisitos do Sistema — Gerenciamento de Fila de Atendimento

## 1. Identificação do Sistema

**Nome:** Sistema de Gerenciamento de Fila de Atendimento

**Tecnologias:** Python, Flask, SQLite, HTML e CSS

**Objetivo:** Desenvolver uma aplicação web capaz de controlar uma fila de atendimento, permitindo cadastrar clientes, visualizar a fila, chamar o próximo cliente, concluir atendimentos e cancelar atendimentos.

---

# 2. Descrição do Sistema

O sistema será utilizado para organizar uma fila de atendimento de clientes.

Cada cliente cadastrado deverá entrar na fila com o status **Aguardando**.

O atendimento deverá seguir a regra **FIFO (First In, First Out)**, garantindo que o primeiro cliente cadastrado seja o primeiro cliente chamado.

O sistema também deverá permitir acompanhar o estado de cada atendimento.

---

# 3. Requisitos Funcionais

Os requisitos funcionais descrevem **o que o sistema deve fazer**.

| ID   | Requisito                   | Descrição                                                                                                   |
| ---- | --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| RF01 | Cadastrar cliente           | O sistema deve permitir cadastrar um novo cliente informando seu nome.                                      |
| RF02 | Inserir cliente na fila     | Após o cadastro, o sistema deve inserir automaticamente o cliente na fila com o status `Aguardando`.        |
| RF03 | Visualizar fila             | O sistema deve permitir visualizar os clientes que estão ou estiveram na fila.                              |
| RF04 | Ordenar fila                | O sistema deve apresentar os clientes seguindo a ordem de chegada.                                          |
| RF05 | Chamar próximo cliente      | O sistema deve permitir chamar o próximo cliente disponível na fila.                                        |
| RF06 | Aplicar FIFO                | O sistema deve selecionar primeiro o cliente que entrou há mais tempo e ainda está com status `Aguardando`. |
| RF07 | Alterar para Em atendimento | Ao chamar um cliente, o sistema deve alterar seu status para `Em atendimento`.                              |
| RF08 | Concluir atendimento        | O sistema deve permitir alterar o status de um atendimento para `Concluído`.                                |
| RF09 | Cancelar atendimento        | O sistema deve permitir cancelar um atendimento.                                                            |
| RF10 | Armazenar dados             | O sistema deve armazenar os dados dos clientes em um banco de dados SQLite.                                 |
| RF11 | Identificar cliente         | Cada cliente deve possuir um identificador único.                                                           |
| RF12 | Registrar entrada           | O sistema deve registrar a data e hora em que o cliente entrou na fila.                                     |

---

# 4. Requisitos Não Funcionais

Os requisitos não funcionais descrevem **como o sistema deve funcionar**.

| ID    | Requisito        | Descrição                                                                                          |
| ----- | ---------------- | -------------------------------------------------------------------------------------------------- |
| RNF01 | Tecnologia       | O sistema deve ser desenvolvido utilizando Python e Flask.                                         |
| RNF02 | Banco de dados   | O sistema deve utilizar SQLite para armazenamento dos dados.                                       |
| RNF03 | Interface web    | O sistema deve possuir uma interface acessível através de um navegador.                            |
| RNF04 | Usabilidade      | A interface deve ser simples e fácil de utilizar.                                                  |
| RNF05 | Desempenho       | As operações de cadastro e consulta devem ser realizadas rapidamente em condições normais de uso.  |
| RNF06 | Organização      | O projeto deve possuir separação entre arquivos HTML, CSS e código Python.                         |
| RNF07 | Compatibilidade  | A aplicação deve funcionar em navegadores modernos.                                                |
| RNF08 | Persistência     | Os dados cadastrados devem permanecer armazenados no banco após o encerramento da aplicação.       |
| RNF09 | Manutenibilidade | O código deve ser organizado de forma que futuras alterações possam ser realizadas com facilidade. |
| RNF10 | Segurança básica | Os dados enviados pelos formulários devem ser tratados pelo backend antes de serem armazenados.    |

---

# 5. Regras de Negócio

As regras de negócio determinam o comportamento da fila.

### RN01 — Entrada na fila

Todo cliente cadastrado deve receber automaticamente o status:

```text
Aguardando
```

---

### RN02 — Ordem de atendimento

O atendimento deve seguir a ordem de chegada dos clientes.

Exemplo:

```text
João → Maria → Carlos
```

João deverá ser chamado antes de Maria, e Maria antes de Carlos.

---

### RN03 — FIFO

O sistema deve considerar somente clientes com status `Aguardando` para determinar o próximo atendimento.

```text
SELECT *
FROM clientes
WHERE status = 'Aguardando'
ORDER BY id ASC
LIMIT 1
```

---

### RN04 — Atendimento

Quando um cliente for chamado, seu status deverá mudar de:

```text
Aguardando
```

para:

```text
Em atendimento
```

---

### RN05 — Conclusão

Quando o atendimento terminar, o status deverá mudar para:

```text
Concluído
```

---

### RN06 — Cancelamento

Um atendimento poderá ser cancelado e deverá receber o status:

```text
Cancelado
```

Clientes cancelados não devem ser chamados novamente.

---

### RN07 — Persistência

Os dados deverão permanecer armazenados no banco de dados SQLite mesmo após o encerramento do servidor.

---

# 6. Casos de Uso

## UC01 — Cadastrar cliente

**Ator:** Atendente

**Objetivo:** Adicionar um cliente à fila.

### Fluxo principal

1. O atendente acessa o sistema.
2. Informa o nome do cliente.
3. Clica em **Entrar na fila**.
4. O sistema valida o nome.
5. O sistema cadastra o cliente.
6. O cliente recebe o status `Aguardando`.
7. O cliente aparece na fila.

---

## UC02 — Visualizar fila

**Ator:** Atendente

**Objetivo:** Visualizar os clientes cadastrados e seus respectivos status.

### Fluxo principal

1. O atendente acessa a página inicial.
2. O sistema consulta o banco de dados.
3. Os clientes são apresentados na tela.
4. Cada cliente apresenta seu status atual.

---

## UC03 — Chamar próximo cliente

**Ator:** Atendente

**Objetivo:** Chamar o próximo cliente da fila.

### Fluxo principal

1. O atendente clica em **Chamar próximo**.
2. O sistema procura clientes com status `Aguardando`.
3. O sistema identifica o cliente mais antigo.
4. O cliente é selecionado.
5. Seu status é alterado para `Em atendimento`.
6. A fila é atualizada.

---

## UC04 — Concluir atendimento

**Ator:** Atendente

**Objetivo:** Finalizar um atendimento.

### Fluxo principal

1. O atendente identifica o cliente em atendimento.
2. Clica em **Concluir**.
3. O sistema altera o status para `Concluído`.
4. O atendimento permanece registrado no banco.

---

## UC05 — Cancelar atendimento

**Ator:** Atendente

**Objetivo:** Cancelar um atendimento.

### Fluxo principal

1. O atendente identifica o cliente.
2. Clica em **Cancelar**.
3. O sistema altera o status para `Cancelado`.
4. O cliente não poderá ser chamado novamente.

---

# 7. Modelo de Dados

A aplicação utilizará a tabela:

```text
clientes
```

Com os seguintes campos:

```text
clientes
│
├── id
├── nome
├── status
└── data_entrada
```

### Dicionário de dados

| Campo          | Tipo     | Obrigatório | Descrição                      |
| -------------- | -------- | ----------- | ------------------------------ |
| `id`           | INTEGER  | Sim         | Identificador único do cliente |
| `nome`         | TEXT     | Sim         | Nome do cliente                |
| `status`       | TEXT     | Sim         | Status atual do atendimento    |
| `data_entrada` | DATETIME | Não         | Data e hora de entrada na fila |

---

# 8. Status do Atendimento

O sistema trabalhará com quatro status principais:

```text
┌──────────────┐
│  Aguardando  │
└──────┬───────┘
       │
       ▼
┌────────────────┐
│ Em atendimento │
└───────┬────────┘
        │
        ▼
┌──────────────┐
│  Concluído   │
└──────────────┘
```

Também existe a possibilidade de:

```text
Aguardando
     │
     ▼
Cancelado
```

---

# 9. Critérios de Aceitação

O sistema será considerado funcional quando:

* [ ] For possível cadastrar um cliente.
* [ ] O cliente aparecer na fila após o cadastro.
* [ ] O novo cliente receber o status `Aguardando`.
* [ ] A fila respeitar a ordem de chegada.
* [ ] O botão **Chamar próximo** selecionar o primeiro cliente aguardando.
* [ ] O cliente chamado receber o status `Em atendimento`.
* [ ] For possível concluir um atendimento.
* [ ] For possível cancelar um atendimento.
* [ ] Clientes concluídos não forem chamados novamente.
* [ ] Clientes cancelados não forem chamados novamente.
* [ ] Os dados forem armazenados no SQLite.
* [ ] Os dados permanecerem disponíveis após reiniciar a aplicação.

---

# 10. Tecnologias e Ferramentas

### Linguagem

**Python**

Utilizada para desenvolver a lógica do sistema.

### Framework

**Flask**

Responsável pelo servidor web, rotas e comunicação entre a interface e o banco de dados.

### Banco de dados

**SQLite**

Utilizado para armazenar os clientes e os dados dos atendimentos.

### Frontend

**HTML5 + CSS3**

Utilizados para construir a interface da aplicação.

### Template Engine

**Jinja2**

Utilizado pelo Flask para apresentar os dados do banco de dados no HTML.

---

# 11. Requisitos para Execução

Para executar o sistema é necessário ter instalado:

* Python 3;
* Flask;
* Navegador web;
* VS Code ou outro editor de código.

### Instalação do Flask

```bash
py -m pip install flask
```

### Execução

```bash
py app.py
```

Depois, acessar:

```text
http://127.0.0.1:5000
```

---

# 12. Resultado Esperado

Ao final, o sistema deverá apresentar uma interface onde o atendente consiga:

```text
┌─────────────────────────────────────┐
│       FILA DE ATENDIMENTO           │
├─────────────────────────────────────┤
│                                     │
│ Nome: [________________]            │
│                                     │
│       [ Entrar na fila ]            │
│                                     │
│       [ Chamar próximo ]            │
│                                     │
├─────────────────────────────────────┤
│ CLIENTES                            │
│                                     │
│ 1  João      Em atendimento         │
│ 2  Maria     Aguardando             │
│ 3  Carlos    Aguardando             │
│                                     │
└─────────────────────────────────────┘
```

O sistema deverá controlar todo o ciclo do atendimento:

```text
Cadastro
   ↓
Aguardando
   ↓
Em atendimento
   ↓
Concluído

ou

Aguardando
   ↓
Cancelado
```

---

# 13. Conclusão

O Sistema de Gerenciamento de Fila de Atendimento demonstra a aplicação prática de conceitos de **desenvolvimento web, banco de dados, operações CRUD, rotas Flask e estruturas de fila**.

A utilização do conceito **FIFO** garante que os clientes sejam atendidos de acordo com sua ordem de chegada, proporcionando uma lógica organizada para o gerenciamento dos atendimentos.
