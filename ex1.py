from decimal import Decimal

def main():
    
    while True:
        print("Digite uma nota: ")
        nota = input()

        if Decimal(nota) >= 0 and Decimal(nota) <= 10:
            print("Nota válida")
            return

        print("Nota inválida")


main()