import random as r
import numpy as np
SIZE = 6
sudoku = []
hor = []
ver = []
square = []

def fill(arr):
    for i in range(SIZE):
        arr.append(i + 1)

def is_there(numb,array):
    for x in range(len(array)):  
        if array[x] == numb:
            return True
        elif x == len(array)-1:
            return False

def sort_hor(arr, a, b):
    index = a
    while index < len(arr):
        jndex = b
        while jndex < len(arr[index]):
            n = r.randint(1, SIZE)
            while is_there(n, arr[index]):
                n = r.randint(1, SIZE)
            arr[index][jndex] = n
            jndex += 2

        index += 2
    
def sort_ver(a, b):
    ind = a
    while ind < len(ver):
        jnd = b

        while jnd < len(ver[ind]):
            n = hor[jnd][ind]
            while is_there(n, ver[ind]) or is_there(n, hor[jnd]):
                n = r.randint(0, SIZE)
            hor[jnd][ind] = n
            ver[ind][jnd] = n  
            jnd += 2

        ind += 2


for i in range(SIZE):
    sudoku.append([])
    hor.append([])
    ver.append([])
    square.append([])


for arr in hor:
    for i in range(SIZE):
        arr.append(0)

for arr in ver:
    for i in range(SIZE):
        arr.append(0)
    
for arr in square:
    for i in range(SIZE):
        arr.append(0)
        


sort_hor(hor, 0, 0)
sort_ver(0, 0)

S = SIZE/3
aux = []
for j in range(3):
    for i in range(S):
        index = i * 3
        while index < (3 + i * 3):
            jndex = j * S
            while jndex < (S + j * S):
                aux.append(hor[index][jndex])
                jndex += 1
            index += 1


square = np.reshape(np.array(aux), (-1, SIZE))

sudoku = hor

aux = []

fill(aux)
delete = []

for i in range(SIZE):
    if is_there(aux[i], hor[0]):
        delete.append(aux[i])

for n in delete:
    aux.remove(n)

print sudoku[0]
print aux

