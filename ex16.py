def fibonacci(n):
      if n == 0:
         return 0
      elif n == 1:
         return 1
      else:
         return fibonacci(n - 1) + fibonacci(n - 2)

def main():

   for i in range(1, 51):
      number = fibonacci(i)
      toStr = str(number)
      print(f"Number: {toStr}")
      if(number > 500):
         break



   
 
main()