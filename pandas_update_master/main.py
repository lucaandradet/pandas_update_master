import pandas as pandas #importando a biblioteca pandas
from datetime import datetime # importando a biblioteca datetime

df = pandas.read_csv("toque.csv") #lendo o arquivo csv

now = datetime.now() #Pegando a data e hora de agora

data_hora = now.strftime("%d/%m/%Y %H:%M:%S") #Definindo formato DD/MM/YYYY HH:MM:SS para a hora pega

#Começando a contar as linhas do csv depois da primeira linha do cabeçalho. Ex. Cabeçalho,0,1,2,3,4,...
df.loc[0, 'UltimaHora'] = data_hora #Atualizando o valor da linha [0], coluna = [UltimaHora] = Data e hora no novo formato

df.to_csv("toque.csv", index=False) #Escrevendo novo valor no arquivo CSV

print(df) #Imprimindo valor inserido no df - DataFrame