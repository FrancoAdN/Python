# from Tkinter import * 
# master = Tk()
# w = Canvas(master, width = 200, height = 100)
# w.pack()

# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill = 'red', dash=(4, 4))
# w.create_rectangle(50, 25, 150, 75, fill='blue')

# mainloop()
# from Tkinter import *

# root = Tk()

# loop = True
# verif = False

# def callback():
#     x_lab = Label(root, text='X: ').pack()
#     x_en = Entry(root).pack()
#     y_lab = Label(root, text='Y: ').pack()
#     y_en = Entry(root).pack()
#     verif = True

 



    

# dim = (1100,600)


# root.title('Graph System')
# root.resizable(width=FALSE, height=FALSE)
# root.geometry('{}x{}'.format(dim[0],dim[1]))

# b_node = Button(root, text = 'ADD NEW NODE',command=callback)
# b_node.pack(side = RIGHT)



# canvas = Canvas(root, width = 800, height = 800, highlightbackground = 'black', highlightcolor='black', highlightthickness=1, bd=0)
# canvas.pack(side=LEFT)



# mainloop()

from Tkinter import *

root = Tk()

def key(event):
    #print "pressed", repr(event.char)
    print event.keycode
    text = str(e.get())
    if(event.keycode > 48 and event.keycode < 59):
        print text
    else:
        text.remove(str(event.keycode))

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y

frame = Frame(root, width=100, height=100)
frame.pack()

e = Entry(frame)
e.bind("<Key>", key)
e.pack()
# e.bind("<Button-1>", callback)


root.mainloop()

