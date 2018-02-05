from sklearn.naive_bayes import MultinomialNB

# [é gordinho?, tem perna curta?, faz "au au"?]
porco1 =    [1, 1, 0]
porco2 =    [1, 1, 0]
porco3 =    [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

# agrupo os animais em um array, 3 porcos seguidos de 3 cachorros
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# uso 1 como indicador de porco e -1 de cachorro
marcacoes = [1, 1, 1, -1, -1,-1]

# animais que eu quero classificar
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

teste = [misterioso1, misterioso2, misterioso3]
resultado_esperado = [-1, 1, -1]

modelo = MultinomialNB()

# treina o modelo e em seguida faz a prediçã
modelo.fit(dados, marcacoes)
resultado = modelo.predict(teste)

# essa subtração de arrays vai subtrair os elementos de mesmo indice e retornar um array com a diferença
diferencas = resultado - resultado_esperado
acertos = [d for d in diferencas if d == 0]

# calcula a taxa de acerto
total_de_acerto = len(acertos) 
total_de_elementos = len(teste)
taxa_de_acerto = 100.0 * total_de_acerto / total_de_elementos

print(taxa_de_acerto)
