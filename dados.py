# -*- coding: utf-8 -*-
import csv

def load_access():
    X = []
    Y = []

    # with open('acesso.csv', 'r') as csv_file:
    #     read = csv.reader(csv_file, delimiter=',')

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

def load_find():

    X = []
    Y = []

    arq = open('cursos.csv', 'rb')
    read = csv.reader(arq)

    read.next()

    for home, busca, logado, comprou in read:
        dataset = [int(home), busca, int(logado)]
        X.append(dataset)
        Y.append(comprou)

    return X, Y


