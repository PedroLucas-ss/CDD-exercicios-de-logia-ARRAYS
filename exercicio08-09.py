nomes = [' '] * 5
senhas = [' '] * 5
cont = 3
mudarSenha = 3

for i in range(5):
    nomes[i] = input("Digite seu nome: ")
    senhas[i] = input("Digite sua senha: ")

nome = input("Digite seu nome para logar: ")
while cont >= 0:
    if nome in nomes:
        for x in range(5):
            if nome == nomes[x]:
                senha = input(f"Usuario {nome} encontrado, por favor digite sua senha: ")
                if senha == senhas[x]:
                    print(f"Bem-vindo {nome}")
                    cont = -1
                else:
                    cont = 3
                    while senha != senhas[x] and cont > 0:
                        senha = input(f"Senha invalidade, vc so tem mais {cont} chances: ")
                        if senha == senhas[x]:
                            print(f"Bem-vindo {nome}")
                            cont = -1
                        else:
                            cont -= 1
                            mudarSenha -= 1
                    if mudarSenha == 0:
                        novaSenha = input("Deseja mudar a senha? (digite s para SIM e qualquer outra tecla para NAO): ")
                        if novaSenha == 's':
                            senhas[x] = input("Digite a nova senha: ")
                            print(f"{nome}, sua nova senha foi cadastrada. a senha nova e {senha[x]} ")
                            cont = -1
                        else:
                            cont = -1
    if cont >= 0:
        nome = input(f"Nome invalido, por favor tente novamente (tentativas restantes) {cont}: ")
        cont -= 1
    if cont < 0:
        break