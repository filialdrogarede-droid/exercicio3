import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

user = input("Usuário: ")
password = input("Senha: ")

query = """
SELECT * FROM users
WHERE username = ?
AND password = ?
"""

cursor.execute(query, (user, password))

result = cursor.fetchone()

if result:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha inválidos.")

conn.close()
