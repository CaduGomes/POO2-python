def main():
   fatorial = int(input("Digite um número: "))
   result = 1
   for i in range(1, fatorial + 1):
      result = result * i
   
   print(f"O fatorial de {fatorial} é {result}")

main()