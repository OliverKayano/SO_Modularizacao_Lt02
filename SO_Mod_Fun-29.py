#Algoritmo Lt01.29

#Inicio.

#Declarar.
invest : int = 0
valor : float = 0.0

def entrada():

  print("1 - Poupança (3% ao mês)")
  print("2 - Renda fixa (5% ao mês)")

  local_invest = int(input("Insira o número do investimento: "))
  local_valor = float(input("Valor do investimento: "))

  return local_invest, local_valor

def main():

  invest, valor = entrada()

  if invest == 1 and valor >= 0:
    valor = valor*1.03
    print(f"Valor corrigido (poupança): {valor:.2f}")

  elif invest == 2 and valor >= 0:
    valor = valor*1.05
    print(f"Valor corrigido (renda fixa): {valor:.2f}")

  else:
    print("Tipo de investimento ou valor inválido.")

if __name__=="__main__":
  main()
#Fim.
     