## Importando  bibliotecas
import pandas as pd
import numpy as np
from tqdm import tqdm  ## Biblioteca utilizada para a construção da barra de carregamento no terminal
from time import sleep ## Biblioteca utilizada para a construção da barra de carregamento no terminal

## Comparamos dois dataframes buscando divergencia nas bolsas dos alunos do df1 para o df2.
print("O script irá comparar as informações de todos os RA's da Panilha 1 com a Planilha 2\n")
Planilha1 = input("Planinha 1: ")
Planilha2 = input("Planilha 2: ")
      
df1 = pd.read_excel(Planilha1) ## Dataframe 1 recebe os dados da planilha 1
df2 = pd.read_excel(Planilha2) ## Dataframe 2 recebe os dados da planilha 2
df = pd.DataFrame() ## Cria-se o dataframe final, que será o resultado do cruzamento dos dados. Ainda está vazio!

Lista = [] 
cont = 0
for x in tqdm(range(df1.shape[0])): ## Faço um for de 0 com a quantidade linhas "shape[0]" que meu dataframe1 tem
    Bolsa = '' ## Varivel será utilizada para gravar a bolsa que o aluno possui na planilha do df2, pois as informações só seram salvas fora do loop do Y.
    DESCONTO_SEMESTREANTERIOR = 0 ## Varivel será utilizada para gravar o desconto do semestre anterior do aluno da planilha do df2.
    sleep(0.01) 
    aux = 0 
    erro = 0 ##Nivel de erro
    for y in range (df2.shape[0]): ## Faço um for de 0 com a quantidade linhas que meu dataframe2 tem
        if df1.RA[x] == df2.RA[y] and ((df1.SERVICO[x] == df2.SERVICO[y]) or (df2.SERVICO[y] == "Matrícula") or (df2.SERVICO[y] == "Rematrícula")) and df1.CODBOLSA[x] == df2.CODBOLSA[y] and df1.DESCONTO[x] == df2.DESCONTO[y]:
            aux = 1 ## Se localizar o aluno no df2, o serviço, codbolsa e desconto for igual, não há divergência. Então seto minha variavel aux como 1.
            break;
        elif df1.RA[x] == df2.RA[y] and ((df1.SERVICO[x] == df2.SERVICO[y]) or (df2.SERVICO[y] == "Matrícula") or (df2.SERVICO[y] == "Rematrícula")) and df1.CODBOLSA[x] == df2.CODBOLSA[y]: 
            erro = 'Porcentual desconto não confere com semestre anterior'
            DESCONTO_SEMESTREANTERIOR = df2.DESCONTO[y]
            Bolsa = df2.BOLSA[y]
        elif df1.RA[x] == df2.RA[y] and ((df1.SERVICO[x] == df2.SERVICO[y]) or (df2.SERVICO[y] == "Matrícula") or (df2.SERVICO[y] == "Rematrícula")):
            erro = 'Bolsa não confere com semestre anterior'
            DESCONTO_SEMESTREANTERIOR = df2.DESCONTO[y]
            Bolsa = df2.BOLSA[y]
    if aux == 0:
        if(Bolsa == ''): ##Se a variavel bolsa for igual a vazio, substituo por NULL.
            Bolsa = 'Null'
        cont = cont + 1
        ## Salvo as informações do aluno que apresentou divergencia do df1 para o df2 em uma lista.
        Lista += [[df1.RA[x]], [df1.ALUNO[x]], [df1.CAMPUS[x]],[df1.SERVICO[x]], [df1.CODTURMA[x]], [df1.BOLSA[x]], [df1.CODBOLSA[x]], [df1.DESCONTO[x]], [erro],[Bolsa], [DESCONTO_SEMESTREANTERIOR]]

## A lista é convertida para uma lista com 'cont' linhas e 10 colunas. Corpo (shape) da minha planilha
Lista = np.reshape(Lista, (cont, 11))
## As informações seram gravadas no meu dataframe df
df = pd.DataFrame(data=Lista, columns = 'RA ALUNO CAMPUS SERVICO CODTURMA BOLSA_SEMESTREATUAL CODBOLSA DESCONTO_SEMESTREATUAL NIVELERRO BOLSA_SEMESTREANTERIOR DESCONTO_SEMESTREANTERIOR'.split())
## Planilha salva como Resultados.xlsx
df.to_excel('Resultados.xlsx', sheet_name='Resultados', index=False)

print("Planilha com os resultados foi gerada na pasta em que o codigo está localizado!")
