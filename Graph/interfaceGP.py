from Tkinter import *
import gui




root = Tk()

dim = (1600, 1000)

root.title('Graph System')
#root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(dim[0],dim[1]))



c_frame = Frame(root, bg = 'white', bd = 5)
c_frame.place(relwidth = 0.7, relheight = 1)

canvas = Canvas(c_frame, bg ='blue')
canvas.place(relwidth = 1, relheight = 1)

tool_frame = Frame(root, bg = 'red')
tool_frame.place(relx = 0.7, relwidth = 0.3, relheight = 1)

new_node_frame = gui.Frame_node(tool_frame)


mainloop()