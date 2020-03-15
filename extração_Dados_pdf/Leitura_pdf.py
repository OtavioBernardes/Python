## O script irá ler  o nome de todos os arquivos da pasta que o usuario informar, posteriormente 
## fara a extração dos dados de todos os arquivos pdfs, selecionará desses dados informações definidas.
## Com as informações selecionadadas, será montado um arquivo excel.

import os 
# pip3 install pdfminer3k
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from urllib.request import urlopen
import pandas as pd #pip3 install pandas
import numpy as np  #pip3 install numpy

df = pd.DataFrame() ## Cria-se o dataframe final, onde será armazenado o resultado. Ainda está vazio!

Caminho = input("Digite o caminho onde está os arquivos em PDF para extração dos dados: ")
Caminho = "/mnt/backup/Development/Portfolio_Local/Python/Extracao_Dados_PDF_p-excel/Dados_pdfs" ## Somente para demonstração
Arquivos = os.listdir(Caminho) ## Listamos todos os arquivos da pasta informada
InformacoesDadaFrame = ''  ## string que irei armazenar as informações que seram gravadas no df

def PesquisaString(Lista, NomePDF): ## Função o que Pesquisa na minha string e retorna os dados
    StringRetorno = NomePDF + ' ' 
    for x in range(len(Lista)):
        if Lista[x] == 'Totais:............': ## Procuro a palavra 'Totais:..............' na string
            for y in range(x+1,x+6): ## Como o relatorio recebido em formato pdf é conhecimento, consigo selecionar sem mais nenhuma condição as informações
                StringRetorno = StringRetorno + Lista[y] + ' '
    return StringRetorno ## retorno a String final
    
def lerPDF(arquivoPDF):
    # PDFResourceManager Usado para armazenar recursos compartilhados
    # como fontes e imagens
    recursos = PDFResourceManager()
    buffer = StringIO()
    layoutParams = LAParams()
    dispositivo = TextConverter(recursos, buffer, laparams=layoutParams)
    process_pdf(recursos, dispositivo, arquivoPDF)
    dispositivo.close()
    conteudo = buffer.getvalue()
    buffer.close()
    return conteudo

for x in range(len(Arquivos)): ## realiza-se um for com a quantidade de arquivos na pasta
    arquivoPDF = open(Caminho+'/'+Arquivos[x], 'rb') ## realiza-se aabertura do documento
    aux = lerPDF(arquivoPDF).split() ## utilizo uma variavel auxilar para guardar os dados que são retornados pela função de leitura
    InformacoesDadaFrame += PesquisaString(aux, Arquivos[x])
    arquivoPDF.close()

InformacoesDadaFrame = InformacoesDadaFrame.split(' ') ## dividi-se a string nos espaços
InformacoesDadaFrame = InformacoesDadaFrame[:len(InformacoesDadaFrame)-1] 
## A lista é convertida para uma lista com 'cont' linhas e 10 colunas. Corpo (shape) da minha planilha
InformacoesDadaFrame = np.reshape(InformacoesDadaFrame,(len(Arquivos), 6))
## As informações seram gravadas no meu dataframe df
df = pd.DataFrame(data=InformacoesDadaFrame, columns = 'Nome_PDF ValorNominal EncargosJM ValorBoleto ValorComissão ValorRepasse'.split())
## Planilha salva como InformacoesDadaFrame.xlsx
df.to_excel(Caminho+'/Dados_PDFs.xlsx', sheet_name='Resultados', index=False)



