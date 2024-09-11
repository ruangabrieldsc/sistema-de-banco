import json
from json import JSONDecodeError


class Usuario:
    def __init__(self, nome, senha, idade, genero):
        self.nome = nome
        self.senha = senha
        self.idade = idade
        self.genero = genero
        self.saldo = 0
        self.id = 0

    def mostrarinformacoes(self):
        print("\n---Detalhes da conta---\n "
              "\n Nome: {}\n Idade: {}\n Gênero: {}\n ID: {}\n".format
              (self.nome, self.idade, self.genero, self.id))

    def deposito(self, quantia):
        if quantia < 1:
            print("O valor do depósito deve ser maior que zero.")
        else:
            self.saldo += quantia
            print("Depósito de R${} concluído.\n"
                  "Seu saldo agora é de: {}".format(quantia, self.saldo))

    def sacar(self, quantia):
        if quantia > self.saldo:
            print("Você está tentando sacar um valor maior que seu saldo.")
        elif quantia < 1:
            print("O valor a ser sacado deve ser maior que zero.")
        else:
            self.saldo -= quantia
            print("Você sacou R${}.\n"
                  "Seu saldo agora é de: {}".format(quantia, self.saldo))

    def mostrarsaldo(self):
        print("Seu saldo atual é de: R${}".format(self.saldo))

    def transformaremdicio(self):
        return {"Nome": self.nome, "Senha": self.senha, "Idade": self.idade, "Genero":
            self.genero, "Saldo": self.saldo, "ID": self.id}


def guardarinfo(arquivo, novainfo):
    lista = lerinfo(arquivo)
    lista.append(novainfo)
    with open(arquivo, "w", encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False)


def lerinfo(arquivo):
    try:
        with open(arquivo, "r", encoding='utf-8') as f:
            jsonlista = json.load(f)
        return jsonlista
    except JSONDecodeError:
        return []


def atualizarinfo(arquivo, lista):
    with open(arquivo, "w", encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False)


def getid(arquivo, usuario):
    lista = lerinfo(arquivo)
    try:
        a = lista[len(lista) - 1]
        b = a["ID"] + 1
        usuario.id = b
    except IndexError:
        usuario.id = 1


def verificarsenha(id, nome, senha):
    lista = lerinfo(Usuarios)
    for x in lista:
        valores = list(x.values())
        if valores[0] == nome and valores[1] == senha and valores[5] == id:
            return valores

    print("Informações incorretas, não foi possível acessar sua conta. ")
    return 0


def Layout(usuario):
    while True:
        escolha = input("O que deseja fazer?\n\nDepositar(D)\n"
                        "Sacar(S)\nMostrar Saldo(M)\nTransferir(T)"
                        "\nVer minhas informações(V)\nLogout(0) ").lower()

        match escolha:
            case "d":
                while True:
                    try:
                        deposito = int(input("Quanto deseja depositar? "))
                        break

                    except ValueError:
                        print("Valor inválido. ")
                        pass
                usuario.deposito(deposito)
                salvarsaldo = usuario.saldo
                lista = lerinfo(Usuarios)
                for x in lista:
                    if x["ID"] == usuario.id:
                        x["Saldo"] = salvarsaldo
                        atualizarinfo(Usuarios, lista)
                        break

            case "s":
                while True:
                    try:
                        sacar = int(input("Quando deseja sacar? "))
                        break

                    except ValueError:
                        print("Valor inválido. ")
                        pass
                usuario.sacar(sacar)
                salvarsaldo = usuario.saldo
                lista = lerinfo(Usuarios)
                for x in lista:
                    if x["ID"] == usuario.id:
                        x["Saldo"] = salvarsaldo
                        atualizarinfo(Usuarios, lista)
                        break

            case "m":
                usuario.mostrarsaldo()

            case "t":

                while True:
                    try:
                        transferir = int(input("Quando deseja transferir? "))
                        break

                    except ValueError:
                        print("Valor inválido. ")
                        pass
                if transferir > usuario.saldo:
                    print("Saldo insuficiente. ")
                else:
                    pessoa = input("ID da pessoa para qual deseja fazer a transferência: ")
                    lista = lerinfo(Usuarios)
                    for x in lista:
                        if str(x["ID"]) == pessoa:
                            x["Saldo"] += transferir
                            atualizarinfo(Usuarios, lista)
                            print("Transferência realizada com sucesso")

                            usuario.saldo -= transferir
                            salvarsaldo = usuario.saldo
                            lista = lerinfo(Usuarios)
                            for x in lista:
                                if x["ID"] == usuario.id:
                                    x["Saldo"] = salvarsaldo
                                    atualizarinfo(Usuarios, lista)
                            break
            case "v":
                usuario.mostrarinformacoes()
            case "0":
                break


Usuarios = "Usuarios.json"

while True:
    escolha = input("\nO que deseja fazer?\n\nLogin(L)\n\nCriar uma nova conta(C)\n\nSair(0): ").lower()
    if escolha != "l" and escolha != "c" and escolha != "0":
        print("\nEscolha inválida\n")
    elif escolha == "0":
        break
    elif escolha == "l":
        while True:
            while True:
                try:
                    id = int(input("Seu ID: "))
                    break
                except ValueError:
                    print("ID inválido")
            nome = input("Seu nome: ").upper()
            senha = input("Sua senha: ")
            info = verificarsenha(id, nome, senha)
            if info == 0:
                break

            User = Usuario(info[0], info[1], info[2], info[3])
            User.saldo = info[4]
            User.id = info[5]
            Layout(User)
            break

    elif escolha == "c":
        while True:
            nome = str(input("Nome: ")).upper()
            if nome.isalpha():
                break
            print("Apenas letras são permitidas.")

        while True:
            senha = input("Senha: ")
            senha2 = input("Confirmar senha: ")
            if senha == senha2:
                break
            print("As senhas não são compatíveis.")

        while True:
            while True:
                try:
                    idade = int(input("Idade: "))
                    break

                except ValueError:
                    print("Idade inválida. ")
                    pass

            if type(idade) is int:
                if 17 < idade < 131:
                    break
            print("Idade inválida.")

        while True:
            genero = input("Gênero(M, F, Nb): ").lower()

            match genero:
                case "m":
                    genero = "Masculino"
                    break
                case "f":
                    genero = "Feminino"
                    break
                case "nb":
                    genero = "Não Binário"
                    break
                case _:
                    print("Gênero inválido. ")

        User = Usuario(nome, senha, idade, genero)
        getid(Usuarios, User)
        guardarinfo(Usuarios, User.transformaremdicio())
        print("Conta criada.\nSeu ID é: {}".format(User.id))
        Layout(User)

