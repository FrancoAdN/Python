import random as r
num = [[],[],[],[],[],[]]

aux = []
aux_dos = [0,0,0,0,0,0]


def is_there(numb,array,exp):
    for x in range(len(array)):  
        if array[x] == numb or exp == numb:
            return True
        elif x == len(array)-1:
            return False


aux.append(r.randint(1,6))
num[0].append(aux[0])

for i in range(5):
    rand = r.randint(1,6)
    while(is_there(rand,aux,0)):
        rand = r.randint(1,6)
    if not(is_there(rand,aux,0)):
        aux.append(rand)
        num[i+1].append(aux[i+1])


for i in range(2):
    for x in range(5):
        rand = r.randint(1,6)
        while(is_there(rand,num[i],0)):
            rand = r.randint(1,6)
        if not(is_there(rand,num[i],0)):
            num[i].append(rand)

aux_dos[0] = num[0][5]
aux_dos[5] = num[1][5]


arr_aux = num[5]
num[5] = num[1]
num[1] = arr_aux

for i in range(4):
    rand = r.randint(1,6)
    while(is_there(rand,aux_dos,num[i+1][0])):
        rand = r.randint(1,6)
    if not(is_there(rand,aux_dos,num[i+1][0])):
        aux_dos[i+1] = rand
        num[i+1].append(rand)

for i in range(4):
    for j in range(4):
        rand = r.randint(1,6)
        while(is_there(rand,num[i+1],0)):
            rand = r.randint(1,6)
        if not(is_there(rand,num[i+1],0)):
            num[i+1].append(rand)

for i in range(4):
    n_aux = num[i+1][1]
    num[i+1][1] = num[i+1][5]
    num[i+1][5] = n_aux




for n in num:
    print(n)
print('\n')

aux = [[],[],[],[],[],[]]

for i in range(6):
    for arr in num:
        aux[i].append(arr[i])


print aux
        
