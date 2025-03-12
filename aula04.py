nivel_acesso = int(input("Digite o nível de acesso (1 a 3): "))

if nivel_acesso == 3:
    print("Acesso total")
elif nivel_acesso == 2:
    print("Acesso parcial")
elif nivel_acesso == 1:
    print("Acesso restrito")
else: 
    print("Nível de acesso inválido")