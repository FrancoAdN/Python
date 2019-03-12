from termcolor import colored
import getch as g
import os
import sys





def print_men(arr,inx):
    for i in range(len(arr)):
        if(i == inx):
            print(colored(arr[i],'blue'))
        else:
            print(arr[i])

def find(wd,arr):
    items = []
    for elm in arr:
        s = elm[0:len(wd)]
        if s == wd:
            items.append(elm)
    return items


def start(lst):
    found = []
    word = ''
    index = 0

    while True:
        ch = g.getch()
        if(ch == '\r'):
            break
        elif(ch == '\t' or ord(ch) == 66):#downarrow
            index += 1
            os.system('clear')
            print word
            print_men(found,index)
        elif(ord(ch) == 27): #esc
            print 'Termino el pedido' 
        elif(ord(ch) == 137):
            word.pop(len(word) - 1)
            word.pop(len(word))
        else:
            os.system('clear')
            word = word + ch
            print word
            found = find(word,lst)
            print_men(found,index)

    os.system('clear')
    try:
        print found[index]
    except:
        print 'No item selected\n'
    
    
