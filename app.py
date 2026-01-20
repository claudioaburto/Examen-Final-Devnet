from flask import Flask, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
DB_NAME = "usuarios.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM usuarios WHERE usuario=?", (usuario,))
        row = cursor.fetchone()
        conn.close()

        if row and check_password_hash(row[0], password):
            return f"Bienvenido {usuario}"
        else:
            return "Usuario o contraseña incorrecta"

    return """
        <h2>Login</h2>
        <form method="post">
            Usuario: <input type="text" name="usuario"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Ingresar">
        </form>
    """

@app.route("/crear")
def crear_usuarios():
    usuarios = {
        "Claudio Aburto": "clave123",
        "usuario2": "password456"
    }

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for u, p in usuarios.items():
        hash_pw = generate_password_hash(p)
        try:
            cursor.execute(
                "INSERT INTO usuarios (usuario, password) VALUES (?,?)",
                (u, hash_pw)
            )
        except:
            pass

    conn.commit()
    conn.close()
    return "Usuarios creados correctamente"

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5800)
