import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot

df = pd.read_excel("AdventureWorks.xlsx")

#Visualizando as primeiras linhas
print (df.head())

#Visualizando tipos de dados
print (df.dtypes)

#Receita total
print ("Receita total: ")
print (df["Valor Venda"].sum())

#Custo Total - Criando uma coluna para visualizar resultado
df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])
print(df.head(1))

#Custo Total
print ("Custo total: ")
print (round(df["Custo"].sum(),2))

#Criando coluna de lucro
df["Lucro"] = df["Valor Venda"] - df["Custo"]

#Visualizando lucro total
print ("Lucro total:")
print (round(df["Lucro"].sum(),2))

#Visualizando tempo de envio
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
print (df.head(1))

#Verificando a média do tempo de envio por Marca
print ("Média de tempo de envio em dias: ")
print (df.groupby("Marca")["Tempo_envio"].mean())

#Verificando o Lucro por ano e por marca.
print ("Lucro por ano e por marca: ")
#configurando o formato dos números flutuantes:
pd.options.display.float_format = '{:20,.2f}'.format
print (df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum());

#Agrupando os dados em colunas
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
print (lucro_ano)

#Verificando a quantidade de produtos vendidos
print ("Quantidade de produtos vendidos:")
print (df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False))

#Gráfico do total de produtos vendidos
grafico1 = (df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title = "Total de produtos Vendidos"))
plt.xlabel("Quantidade")
plt.ylabel("Produto")
plt.savefig("grafico1.png")
pyplot.close("grafico1.png")

#Gráfico de lucro por ano
df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title="Lucro por ano")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.savefig("grafico2.png")

#Vendas por ano - 2009:
df_2009 = df[df["Data Venda"].dt.year == 2009]
df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title="Lucro por mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.savefig("grafico3.png")

#Lucro por marca
df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title="Lucro por marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');#alterando a rotação do subtítulo do eixo X
plt.savefig("grafico4.png")

#Agrupando resultados por classe:
df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title="Lucro por classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');#alterando a rotação do subtítulo do eixo X
plt.savefig("grafico5.png")

#Fazendo algumas análises estatísticas
print(df["Tempo_envio"].describe)

#gráfico de boxplot
grafico6 = plt.boxplot(df["Tempo_envio"]);
plt.xlabel("Dias")
plt.xticks(rotation='horizontal');#alterando a rotação do subtítulo do eixo X
plt.savefig("grafico6.png")
#Com esse tipo de gráfico podemos visualizar outliers e podemos fazer as análises usando:
#tempo de envio mínimo:
print (df["Tempo_envio"].min())
print (df["Tempo_envio"].max())
print (df[df["Tempo_envio"] == 20])

#Histograma do tempo de envio
plt.hist(df["Tempo_envio"])
plt.xlabel("Dias")
plt.xticks(rotation='horizontal');#alterando a rotação do subtítulo do eixo X
plt.savefig("grafico7.png")

#Salvando o arquvo com as análises
df.to_csv("df__analise_vendas.csv", index=False)
