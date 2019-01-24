art=[] #array tipo diccionario de los articulos
pedidos=[] #array tipo diccionario de los pedidos que se ingresan en el dia
pedidos.append({'n':'N°ART','nombre':'NOMBRE','cant':'CANTIDAD','precio':})
def aItemP():





def getArt():
    file = open('art.csv','r')
    i=0
    for line in file:
        aux=line.split(',')
        art.append({'nombre':'a','precio':0})
        art[i]['nombre'] = str(aux[0])
        try:
            art[i]['precio'] = int(aux[1])
        except Exception as e:
            art[i]['precio'] = str(aux[1])
        print(art[i])
        i+=1
    file.close()




def aPedido():
    fin = open('resume.csv','w')
    for item in pedidos:
        fin.write(item)
    fin.close()

'''
fin = open('result.csv','w')
fin.write('No hubo ganancia,franco,2018,claseA')
fin.close()
'''
