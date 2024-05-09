def loginUsuario(perfil):
    if perfil.lower() == "admin":
        print("Bem-vindo, Administrador")
    else:
        print("Bem-vindo, Usuário")

usuario = ("Admin", "admin", "User", "usuário", "etc")

for item in usuario:
    loginUsuario(item)