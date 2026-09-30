from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "fila.db"


def conectar_banco():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Aguardando',
            data_entrada DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexao.commit()
    conexao.close()


@app.route("/")
def index():
    conexao = conectar_banco()

    clientes = conexao.execute("""
        SELECT * FROM clientes
        ORDER BY id ASC
    """).fetchall()

    conexao.close()

    return render_template("index.html", clientes=clientes)


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"].strip()

    if nome:
        conexao = conectar_banco()

        conexao.execute("""
            INSERT INTO clientes (nome, status)
            VALUES (?, 'Aguardando')
        """, (nome,))

        conexao.commit()
        conexao.close()

    return redirect("/")


@app.route("/chamar-proximo", methods=["POST"])
def chamar_proximo():
    conexao = conectar_banco()

    cliente = conexao.execute("""
        SELECT * FROM clientes
        WHERE status = 'Aguardando'
        ORDER BY id ASC
        LIMIT 1
    """).fetchone()

    if cliente:
        conexao.execute("""
            UPDATE clientes
            SET status = 'Em atendimento'
            WHERE id = ?
        """, (cliente["id"],))

        conexao.commit()

    conexao.close()

    return redirect("/")


@app.route("/concluir/<int:id>", methods=["POST"])
def concluir(id):
    conexao = conectar_banco()

    conexao.execute("""
        UPDATE clientes
        SET status = 'Concluído'
        WHERE id = ?
    """, (id,))

    conexao.commit()
    conexao.close()

    return redirect("/")


@app.route("/cancelar/<int:id>", methods=["POST"])
def cancelar(id):
    conexao = conectar_banco()

    conexao.execute("""
        UPDATE clientes
        SET status = 'Cancelado'
        WHERE id = ?
    """, (id,))

    conexao.commit()
    conexao.close()

    return redirect("/")


if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)