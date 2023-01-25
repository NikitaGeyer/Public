from tkinter import *
root = Tk()
root.title('Домик и солнышко')
root.geometry('800x650')

canvas = Canvas(root, width=500, height=450, bg='white')
canvas.pack()

def color1():
    canvas.itemconfig(oval, fill='orange', outline='')
def color2():
    canvas.itemconfig(rectangle, fill='light green')
def color3():
    canvas.itemconfig(polygon, fill='pink')


rectangle3 = canvas.create_rectangle(0, 0, 600, 350, fill='cyan')
rectangle2 = canvas.create_rectangle(0, 350, 600, 450, fill='green', outline='')
oval = canvas.create_oval(380, 5, 495, 120, width=5, fill='yellow', outline='yellow')
rectangle = canvas.create_rectangle(175, 300, 325, 450, width=5, fill='grey', outline='')
polygon = canvas.create_polygon(175, 299, 250, 225, 325, 299, fill='light blue', outline='')


b1 = Button(root, text='Солнышко', command=color1)
b1.pack()
b2 = Button(root, text='Стены', command=color2)
b2.pack()
b3 = Button(root, text='Крыша', command=color3)
b3.pack()

root.mainloop()
