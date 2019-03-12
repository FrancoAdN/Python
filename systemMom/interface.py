from Tkinter import *


def makePercent(size, per):
    return (per*size)/100

def func(event):
    print 'enter'


class DimF:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y


dim = (1280,900)


root = Tk()
root.title('More Clean System')
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(dim[0],dim[1]))


#LEFT FRAME THINGS
leftF = DimF(makePercent(15, dim[0]), makePercent(100, dim[1]), x = 0, y = 0)
f_left = Frame(root,bg='green',width = leftF.width , height = leftF.height).place( x = leftF.x, y = leftF.y)


#TOP FRAME THINGS
topF = DimF(makePercent(75, dim[0]), makePercent(10, dim[1]), leftF.width, 0)
f_top = Frame(root,bg='blue',width = topF.width, height = topF.height).place(x = topF.x, y = topF.y)
i = PhotoImage(file = 'logoMC.png')
logoIm = Label(root, image = i, width = topF.width, height = 100).pack()


#RIGHT FRAME THINGS
rightF = DimF(makePercent(10, dim[0]), leftF.height, leftF.width + topF.width, 0)
f_right = Frame(root,bg='red', width = rightF.width, height = rightF.height).place(x = rightF.x, y = rightF.y)


#BOTTOM FRAME THINGS
botF = DimF(topF.width, topF.height, topF.x, dim[1] - topF.height)
f_bottom = Frame(root,bg='yellow',width = botF.width, height = botF.height).place(x = botF.x, y = botF.y)


#CENTRAL FRAME THINGS
centralF = DimF(topF.width, botF.y - botF.height, leftF.width, topF.height)
f_center = Frame(root, bg = 'white', width = centralF.width, height = centralF.height).place(x = centralF.x, y = centralF.y)


search = Entry(root,bg='white',fg='black')
search.place(x = centralF.x, y = centralF.y, width = centralF.width, height = 35)
root.bind('<Return>',func)


scroll = Scrollbar(f_center)
scroll.place(x = rightF.x - 15, y = centralF.y, height = centralF.height)


products = Listbox(f_center,yscrollcommand = scroll.set)
for line in open('stock_local.csv','r'):
    products.insert(END,line)
products.place(x = centralF.x, y = centralF.y + 35, width = centralF.width - 20, height = centralF.height - 35)


scroll.config(command = products.yview)


root.mainloop()



