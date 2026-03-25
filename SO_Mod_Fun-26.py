
#Algoritmo Lt01.26.

#Inicio.

def main():

   #Declarar variáveis locais.
   num1 : int = 0
   num2 : int = 0

   num1, num2 = map(int, input("Insira 2 números inteiros, separados por espaço: ").split())
   divisão(num1, num2)

def divisão(num1, num2):
   if num1 >= num2:

      if num1 % num2 == 0:
         print(num1, "é múltiplo de ",num2)

      else:
         print(num1,"não é múltiplo de ",num2)

   elif num2 % num1 == 0:
      print(num2,"é múltiplo de ",num1)

   else:
      print(num2,"não é múltiplo de ",num1)

if __name__=="__main__":
   main()

#Fim.