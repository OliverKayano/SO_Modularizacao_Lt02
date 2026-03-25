#Algoritmo Lt01_27.

#Iniciar.

def main():

   #Declarar variáveis locais:
   voltas : float = 0
   metros : float = 0
   tempo : float = 0

   voltas, metros, tempo = map(float, input("Insira o número de voltas, extensão do circuito (em metros), e tempo (em minutos), separados por espaço: ").split())
   velocidade(voltas, metros, tempo)

def velocidade(voltas, metros, tempo):
   #Declarar variáveis locais:
   vel_md : float = 0

   voltas = voltas*metros/1000
   tempo = tempo/60
   vel_md = voltas/tempo

   print("Velocidade média do percurso: ",vel_md,"km/h")

if __name__=="__main__":
   main()

#Fim.