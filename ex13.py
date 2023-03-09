def exponencial(base, expoente):
   result = 0
   if (expoente == 0):
      return 1
   for i in range(expoente):
         if (i == 0):
            result = base
         else:
            result = result * base
   return result

def main():
   base = int(input("Digite a base: "))
   expoente = int(input("Digite o expoente: "))

   result = exponencial(base, expoente)

   toStr = str(result)
   print(f"Resultado: {toStr}")

main()