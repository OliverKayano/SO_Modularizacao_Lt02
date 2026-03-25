
#Algoritmo_Lt01.22.

#Declarar.
num1 : int = 0
num2 : int = 0

#Inicio.

def main():
   global num1
   global num2

   num1, num2 = map(int, input("Insira 2 números inteiros (separados por espaço): ").split())

   ordem(num1, num2)

def ordem(num1, num2):
   if num1 > num2:
      print ("Ordem crescente: ", num2, ",", num1)

   else:
      print ("Ordem crescente: ", num1, ",", num2)

if __name__=="__main__":
   main()

#Fim.