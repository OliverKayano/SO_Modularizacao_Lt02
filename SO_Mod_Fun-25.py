
# Algoritmo Lt01.25.

#Inicio.

def main():

# Declarar variáveis locais:
   Hora_i : int = 0
   Hora_f : int = 0
   min_i : int = 0
   min_f : int = 0

   Hora_i , min_i = map(int, input("Horário inicial do jogo, no formato HH:mm: ").split(":"))
   Hora_f , min_f = map(int, input("Horário final do jogo, no formato HH:mm: ").split(":"))

   hora(Hora_i, Hora_f, min_i, min_f)

def hora(Hora_i, Hora_f, min_i, min_f):

#Declarar variáveis locais:
   Hora_t : int = 0
   min_t : int = 0

   if Hora_i <= Hora_f:
      Hora_t = Hora_f - Hora_i

   else:
      Hora_t = 24 + Hora_f - Hora_i

   if min_i <= min_f:
      min_t = min_f - min_i

   else:
      min_t = 60 + min_f - min_i
      Hora_t = Hora_t - 1

   print("Tempo de jogo: ", Hora_t,":",min_t)

if __name__=="__main__":
   main()

#Fim.