from tkinter import *
root = Tk()


def myClick():
    #my_label = Label(root,text="SURPRISE",fg="green",padx=10,pady=10).pack()
    e = Entry(root,width=50,fg="gray").pack()

my_button = Button(root,text="CLICK ME",command= myClick,fg="yellow",bg="blue",padx=30,pady=20).pack()
#my_label.grid(row = 0, column = 0)
root.mainloop()