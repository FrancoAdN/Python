import datetime as d
from termcolor import colored
import pedido
import getch as g
import os
import sys

lst = ['trapo','lavandina','lavanda','desodorante','papel','panda','lagartija']

menu = ['Hacer pedido','Ver facturacion','Ver stock','Buscar producto','Salir']

def h_pedido():
    print 'Hacer pedido'
    os.system('clear')
    pedido.start(lst)


def v_fact():
    print 'Ver facturacion'

def v_stock():
    print 'Ver stock'

def b_producto():
    print 'Ver producto'





def p_menu():
    inx = 0
    while True:
        os.system('clear')
        date = str(d.datetime.now()).split('.')
        date = date[0]
        print 'BIENVENIDO\t\t\t' + date

        print '\r'
        for i in range(len(menu)):
            if(i == inx):
                print(colored(menu[i],'blue'))
            else:
                print menu[i]
        
        ch = g.getch()
        if(ord(ch) == 66):
            inx += 1
        elif(ch == '\r' and inx == 0):
            h_pedido()
            break
        elif(ch == '\r' and inx == 1):
            v_fact()
            break
        elif(ch == '\r' and inx == 2):
            v_stock()
            break
        elif(ch == '\r' and inx == 3):
            b_producto()
            break
        elif(ch == '\r' and inx == 4):
            break
        elif(ch == '\r'):
            break
        



p_menu()