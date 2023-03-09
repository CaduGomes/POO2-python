def main():
    maior = 0
    for i in range(1,6):
        toStr = str(i)
        num = input(f"Digite o {toStr}º número: ")

        if float(num) > maior:
            maior = float(num)
    
    toStr = str(maior)
    print(f"O maior número é: {toStr}")

main()