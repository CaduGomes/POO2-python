def main():
    soma = 0
    media = 0
    for i in range(1,6):
        toStr = str(i)
        num = input(f"Digite o {toStr}º número: ")

        soma += float(num)

    media = soma / 5   
    toStr = str(soma)
    print(f"Soma: {toStr}")

    toStr = str(media)
    print(f"Media: {toStr}")

main()