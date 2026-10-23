user = input("Usuário: ")
password = input("Senha: ")

query = (
    "SELECT * FROM users "
    "WHERE username = '" + user +
    "' AND password = '" + password + "'"
)
