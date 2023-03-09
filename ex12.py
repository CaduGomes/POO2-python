def tabuada(num):
   for i in range(1,11):
      print(f"{num} x {i} = {num * i}")

def main():
   num = int(input("Digite um número: "))
   tabuada(num)
main()