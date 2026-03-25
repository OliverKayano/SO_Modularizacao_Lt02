#Algoritmo ModFun_Lt02.21.

#Declarar.
media : float = 0.0
n1 : float = 0.0
n2 : float = 0.0
n3 : float = 0.0
n4 : float = 0.0

#Início.

def main():
   global n1
   global n2
   global n3
   global n4
   global media

   n1, n2, n3, n4 = map(float, input ("Insira as 4 notas do aluno (separadas por espaço): ").split())
   media = (n1 + n2 + n3 + n4) / 4

   verificação(media)

def verificação (media):

   if media >= 6.0:
      print ("Nota: ", media, "Aprovado")

   elif media >= 3.0:
      print ("Nota: ", media, "Exame")

   else:
      print ("Nota: ", media, "Retido")

if __name__=="__main__":
   main()

#Fim.
     