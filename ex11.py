def main():
   num1 = input("Digite o primeiro número: ")
   num2 = input("Digite o segundo número: ")
   soma = 0
   for i in range(int(num1) + 1, int(num2)):
      print(i, end=" ")
      soma += i

   toStr = str(soma)
   print(f"\nSoma: {toStr}")
main()