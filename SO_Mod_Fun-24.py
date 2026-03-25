
#Algoritmo Lt01.24.

#Declarar.
n : int = 0

#Inicio.

def main():
   n = int(input("Insira um número inteiro: "))
   divisão(n)

def divisão(n):

   if n % 6 == 0:
      print("Valor divisível por 2 e 3")

   else:
      print("Não divisível por 2 e 3")

if __name__=="__main__":
   main()

#Fim.