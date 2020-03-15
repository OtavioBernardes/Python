import numpy as np # importando a biblioteca Numpy
Moedas = np.array([]) # Array com as Moedas Disponvieis
QuantMoedas = int(input("Digite a variedade de moedas disponiveis para troco: "))

for i in range(0,QuantMoedas): 
    Moedas = np.append(Moedas, int(input("Digite quais moedas estão disponiveis para o troco: ")))
Moedas = -np.sort(-Moedas) # Ordeno minha lista em ordem decrescente 

def CalculaTroco(Troco, i):  # i: é o contador para passar para a proxima moeda
    while(Troco != 0): # Meu while sera executado enquanto meu troco for diferente de 0
        if(Troco >= Moedas[i]): # Se meu troco for maior ou igual a Moeda na posição do contador, executo os comandos do IF
            aux = int(Troco/Moedas[i]) # Calculo a quantidade maxima de moedas[i] que consigo utilizar no troco, pegando a parte inteira da divisão
            print("Foram usadas ",aux," moedas de", Moedas[i], "centavos") # printo quantas moedas foram utilizadas da moeda da posição I
            Troco = (Troco - (aux*Moedas[i])) # Subtraio do troco o valor calculado acima, Quantidade de Moedas * Moedas na posição I
        i = i + 1 # Passo para a proxima moeda 
    
Valor_Troco = int(input("Informe o valor do troco em centavos: ")) #Recebo do usuario o troco em centavos
CalculaTroco(Valor_Troco, 0) #Calcula e printa as moedas do troco |  Passo para função o troco informado e a posição inicial do contador