def main():
    
    populacaoA = 80000
    populacaoB = 200000

    taxaA = 0.03
    taxaB = 0.015

    anos = 0

    while True:
        populacaoA = populacaoA + (populacaoA * taxaA)
        populacaoB = populacaoB + (populacaoB * taxaB)
        anos = anos + 1

        if populacaoA > populacaoB:
            break

    print("População A: ", populacaoA)
    print("População B: ", populacaoB)
    print("Anos: ", anos)


main()