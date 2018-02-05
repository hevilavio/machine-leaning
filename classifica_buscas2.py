import pandas as pd
from collections import Counter

df = pd.read_csv('buscas2.csv')

# extraindo 3 colunas
X_df = df[['home', 'busca', 'logado']]
# extraindo  a 4ª coluna
Y_df = df['comprou']

# extraindo o 'dummies' da coluna 'busca' (transforma a coluna da string de busca em N outras colunas,
# sendo N igual ao numero distinto de valores na coluna)
Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

# print((Xdummies_df))

X = Xdummies_df.values
Y = Ydummies_df.values

porcentagem_de_treino = 0.9

tamanho_do_treino = int(porcentagem_de_treino * len(Y))
tamanho_do_teste = len(Y) - tamanho_do_treino

treino_dados = X[:tamanho_do_treino]
treino_marcacoes = Y[:tamanho_do_treino]

teste_dados = X[-tamanho_do_teste:]
# eh esse dado que queremos prever com o algoritmo
teste_marcacoes = Y[-tamanho_do_teste:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()

modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)

acertos = resultado == teste_marcacoes

quantidade_acertos = sum(acertos)
total_de_elementos = len(teste_dados)

taxa_acertos = 100 * quantidade_acertos / total_de_elementos


acerto_base = max(Counter(teste_marcacoes).values())
taxa_de_acerto_base = 100 * acerto_base / len(teste_marcacoes)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)


print(taxa_acertos)
print(total_de_elementos)
