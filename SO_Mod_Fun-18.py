#Algoritmo ModFun_Lt02.18.

#Inicio.

def diferenca(v1, v2):
    d = 0

    if (v1>v2):
        d = (v1-v2);
        print ("diferenca: ", d);
    elif (v2>v1):
        d = (v2-v1);
        print ("diferenca: ", d);
    else:
        print ("diferenca: ", 0);
    #Fim-se;

#Fim-segue.

def main():
    v1 : int = 0
    v2 : int = 0

    v1 = int(input("Insira o primeiro valor: "));
    v2 = int(input("Insira o segundo valor: "));

    diferenca(v1, v2);

if __name__== "__main__":
    main()
#Fim-se;

#Fim.