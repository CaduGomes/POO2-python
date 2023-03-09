def main():
    
    while True:
        print("Digite seu nome: ")
        nome = input()

        print("Digite sua senha: ")
        senha = input()

        if nome == senha:
            print("Nome e senha não podem ser iguais")
            continue
        else:
            print("Nome e senha válidos") 
            break
        


main()