from Tkinter import *

class Frame_node:
    def __init__(self, place):
        self.tool_frame = place
        self.new_node_frame = Frame(self.tool_frame, bg = 'white')
        self.new_node_frame.place(relx = 0.1, rely =  0.04, relwidth = 0.8, relheight = 0.2)

        self.name_node = Label(self.new_node_frame, text = 'Name')
        self.name_node.place(rely = 0.05, relwidth = 0.3)

        self.name_e = Entry(self.new_node_frame)
        self.name_e.insert(0, 'A')
        self.name_e.place(relx = 0.3, rely = 0.05, relwidth = 0.6)

        self.l_x = Label(self.new_node_frame, text = 'X: ')
        self.l_x.place(rely = 0.25, relwidth = 0.3)

        self.e_x = Entry(self.new_node_frame)
        self.e_x.insert(0, '560')
        self.e_x.place(relx = 0.3, rely = 0.25, relwidth = 0.6)

        self.l_y = Label(self.new_node_frame, text = 'Y: ')
        self.l_y.place(relwidth = 0.3, rely = 0.45)

        self.e_y = Entry(self.new_node_frame)
        self.e_y.insert(0, '560')
        self.e_y.place(relx = 0.3, rely = 0.45, relwidth = 0.6)

        self.color_l = Label(self.new_node_frame, text = 'Color: ')
        self.color_l.place(rely = 0.65, relwidth = 0.3)

        self.color_e = Entry(self.new_node_frame)
        self.color_e.insert(0, 'white')
        self.color_e.place(rely = 0.65, relx = 0.3, relwidth = 0.6)

        self.add_node = Button(self.new_node_frame, text = 'Add new node', 
        command = lambda : self.new_node(self.name_e.get(), self.e_x.get(), self.e_y.get(), self.color_e.get()))
        self.add_node.place(rely = 0.85, relx = 0.5, relwidth = 0.5)

        self.remove_node = Button(self.new_node_frame, text = 'Remove node')
        self.remove_node.place(rely = 0.85, relwidth = 0.5)

    def new_node(self, name, x, y, color):
        if ((not name) and (not color)):
            if((not x) and (not y)):
                print 'ERROR EN EL INGRESO DEL NODO'
            elif (float(x) and float(y)):
                print float(x)
                print float(y)
            else:
                print 'Error en el ingreso del nodo'
        elif (float(x) and float(y)):
            print name
            print float(x)
            print float(y)
            print color
        else:
            print 'Error en el ingreso del nodo'
            
                
            
        # print name
        # print type(name)
        # print x
        # print type(x)
        # print y
        # print type(y)
        # print color
        # print type(color)
        # self.e_x.delete(0, END)
        # self.e_y.delete(0, END)
        # self.name_e.delete(0, END)
        # self.color_e.delete(0, END)