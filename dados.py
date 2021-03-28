import csv

def load_access():
    X = []
    Y = []

    arq = open('acesso.csv', 'rb')
    read = csv.reader(arq)

    read.next()
    
    for home,como_funciona,contato,comprou in read:
        dado = [int(home),int(como_funciona),int(contato)]
        X.append(dado)
        Y.append(int(comprou))

    return X, Y

# x, y = load_access()
# print(x)