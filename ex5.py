from decimal import Decimal

def main():
    populacaoA = 0
    populacaoB = 0

    taxaA = 0
    taxaB = 0


    while True:
        if populacaoA == 0:
            populacaoA = input("Digite a população A: ")

            try:
                populacaoA = int(populacaoA)

                if populacaoA <= 0:
                    print("População inválida")
                    populacaoA = 0
                    continue
            except:
                print("População inválida")
                populacaoA = 0
                continue

        if populacaoB == 0:
            populacaoB = input("Digite a população B: ")
        
            try:
                populacaoB = int(populacaoB)

                if populacaoB <= 0:
                    print("População inválida")
                    populacaoB = 0
                    continue
            except:
                print("População inválida")
                populacaoB = 0
                continue

        if taxaA == 0:
            taxaA = input("Digite a taxa de crescimento da população A: ")

            try:
                taxaA = float(taxaA)

                if taxaA < 0:
                    print("Taxa inválida")
                    taxaA = 0
                    continue
            except:
                print("Taxa inválida")
                taxaA = 0
                continue

        if taxaB == 0:
            taxaB = input("Digite a taxa de crescimento da população B: ")

            try:
                taxaB = float(taxaB)

                if taxaB < 0:
                    print("Taxa inválida")
                    taxaB = 0
                    continue
            except:
                print("Taxa inválida")
                taxaB = 0
                continue

        anos = 0

        while True:
            populacaoA = populacaoA + (populacaoA * taxaA)
            populacaoB = populacaoB + (populacaoB * taxaB)
            anos = anos + 1

            if populacaoA > populacaoB:
                print("População A: ", populacaoA)
                print("Anos: ", anos)
                print("População B: ", populacaoB)
                populacaoA = 0
                populacaoB = 0
                taxaA = 0
                taxaB = 0
                break


main()