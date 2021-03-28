from dados import load_access

x, y = load_access()

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(x, y)

acesso1 = [1,0,1]
acesso2 = [0,1,0]
test = [acesso1,acesso2]

result_predict = model.predict(test)
print('test',result_predict)

## aqui ele está treinando e testando com os mesmos dados então o resultado será alto nos acerto diferente com dados desconhecidos

result_x = model.predict(x)

diferencas = result_x - y

acertos = [d for d in diferencas if d == 0]

total_acertos = len(acertos)
total_element = len(x)

taxa_acerto = 100.0 * total_acertos / total_element
print('taxa_acerto',taxa_acerto)
print('total_element',total_element)

# print('result_x',result_x)

# result_y = model.predict(y)
# print('result_y',result_y)