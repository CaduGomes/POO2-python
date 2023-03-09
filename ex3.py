
from decimal import Decimal

def main():    
    nome = ""
    idade = 0
    salario = 0
    sexo = ""
    estado_civil = ""

    while True:

        if nome == "":
            print("Digite seu nome: ")
            nome = input()

        if len(nome) <= 3:
            print("Nome deve ter mais de 3 caracteres")
            nome = ""
            continue

        if idade == 0:
            print("Digite sua idade: ")
            idade = input()

        if Decimal(idade) < 0 or Decimal(idade) > 150:
            print("Idade inválida")
            idade = 0
            continue

        if salario == 0:
            print("Digite seu salário: ")
            salario = input()

        if Decimal(salario) < 0:
            print("Salário inválido")
            salario = 0
            continue

        if sexo == "":
            print("Digite seu sexo: ")
            sexo = input()

        if sexo.lower() != "m" and sexo.lower() != "f":
            print("Sexo inválido")
            sexo = ""
            continue

        if estado_civil == "":
            print("Digite seu estado civil: ")
            estado_civil = input()

        if estado_civil.upper() != "S" and estado_civil.upper() != "C" and estado_civil.upper() != "V" and estado_civil.upper() != "D":
            print("Estado civil inválido")
            estado_civil = ""
            continue

        print("Nome: ", nome)
        print("Idade: ", idade)
        print("Salário: ", salario)
        print("Sexo: ", sexo)
        print("Estado civil: ", estado_civil)
        break


main()