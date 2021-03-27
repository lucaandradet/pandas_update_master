import csv #importando a biblioteca CSV
import pandas as pandas #importando a biblioteca pandas
from datetime import datetime # importando a biblioteca datetime

df = pandas.read_csv("toque.csv", engine='python', sep=';', encoding='utf8') #lendo o arquivo csv com delimitador (;)

now = datetime.now() #Pegando a data e hora de agora

data_hora = now.strftime("%d/%m/%Y %H:%M:%S") #Definindo formato DD/MM/YYYY HH:MM:SS para a hora pega

#Começando a contar as linhas do csv depois da primeira linha do cabeçalho. Ex. Cabeçalho,0,1,2,3,4,...
df.loc[1, 'UltimaHora'] = data_hora #Atualizando o valor da linha [0], coluna = [UltimaHora] = Data e hora no novo formato

df.to_csv("toque.csv", index=False, sep=';', encoding='utf8') #Escrevendo novo valor no arquivo CSV com delimitador (;)

print(df) #Imprimindo valor inserido no df - DataFrame
