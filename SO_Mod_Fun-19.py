
#Algoritmo Lt01.19.
#Declarar.
v1 : float = 0; 
v2 : float = 0; 
#Inicio.

def main():
    v1 = int(input("Insira o primeiro valor: "));
    v2 = int(input("Insira o segundo valor: "));
    ajuste(v1, v2)
   
def ajuste(v1, v2):
    
    if (v1>v2):
        print ("Maior valor: ", v1);
    else:
        print ("Maior valor: ", v2);

if __name__=="__main__":
    main()

#Fim.
