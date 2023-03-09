def main():
   quantImpares = 0
   quantPares = 0

   for i in range(10):
      num = int(input("Digite um número: "))
      if (num % 2 != 0):
         quantImpares += 1
      else:
         quantPares += 1

   pares = str(quantPares)

   print(f"Quantidade de números pares: {pares}")

   impares = str(quantImpares)

   print(f"Quantidade de números impares: {impares}")
  

main()