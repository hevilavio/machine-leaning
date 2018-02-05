import pandas as pd
from sklearn.naive_bayes import MultinomialNB


# Previsão de escolha de hostel, com base em dados históricos.
# O Algoritmo vai tentar adivinhar se eu vou gostar de um hostel, tomando como base 
# um csv com informacoes dos hosteis que eu gostei ou não.

df = pd.read_csv('meu_exemplo.csv')

X_df = df[['cafe_da_manha','banheiro_privativo','perto_da_praia','boas_recomendacoes','preco']]
Y_df = df['gostei']

X_dummies = pd.get_dummies(X_df)
Y_dummies = Y_df

X = X_dummies.values
Y = Y_dummies.values

modelo = MultinomialNB()

modelo.fit(X, Y)

# dados com as colunas ja quebradas (no formato dummies)
hostel_1 = [[1, 1, 1, 1, 1, 0, 0]]
hostel_2 = [[0, 1, 1, 1, 0, 0, 1]]
hostel_3 = [[1, 1, 1, 1, 0, 1, 0]]
hostel_4 = [[1, 1, 0, 1, 1, 0, 0]]
hostel_5 = [[1, 1, 0, 1, 0, 0, 1]]
hostel_6 = [[1, 0, 1, 1, 1, 0, 0]]
hostel_7 = [[1, 0, 1, 0, 1, 0, 0]]


print("hostel que tem tudo e eh barato. Vou gostar? %s" % modelo.predict(hostel_1))
print("   ''   '' nao tem café e é caro. Vou gostar? %s" % modelo.predict(hostel_2))
print("   ''   '' tem tudo por preco medio. Vou gostar? %s" % modelo.predict(hostel_3))
print("   ''   '' nao eh perto da praia mas eh barato. Vou gostar? %s" % modelo.predict(hostel_4))
print("   ''   '' nao eh perto da praia e é caro. Vou gostar? %s" % modelo.predict(hostel_5))
print("   ''   '' nao eh perto da praia, tem banheiro e é barato. Vou gostar? %s" % modelo.predict(hostel_6))
print("   ''   '' o mesmo acima, mas nao tem boas recomendações. Vou gostar? %s" % modelo.predict(hostel_7))


#print(X_dummies)
#print(Y_df)