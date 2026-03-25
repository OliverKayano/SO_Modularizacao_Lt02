
#Algoritmo_Lt01.23.

#Declarar.
n1 : float = 0.0
n2 : float = 0.0
n3 : float = 0.0
n4 : float = 0.0

#Inicio.

def main():

   n1, n2, n3 = map(float, input("Insira 3 valores em ordem crescente, separados por espaço: ").split())
   n4 = float(input("Insira um valor aleatório: "))

   ordem(n1, n2, n3, n4)

def ordem(n1, n2, n3, n4):

   if n1 <= n2 and n2 <= n3:

      if n4 <= n1:
         print("Ordem crescente: ", n4,",", n1,",", n2,",", n3)

      elif n4 <= n2:
         print("Ordem crescente: ", n1,",", n4,",", n2,",", n3)

      elif n4 <= n3:
         print("Ordem crescente: ", n1,",", n2,",", n4,",", n3)

      else:
         print("Ordem crescente: ", n1,",",n2,",",n3,",",n4)

   else:
      print("Ordem inválida")

if __name__=="__main__":
   main()

#Fim.