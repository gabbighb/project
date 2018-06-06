from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("gabbi system")

text_Input = StringVar()
Tops = Frame(root, width = 1600,height = 50,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800,height = 700,bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 3600,bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)
#=====================================time=================
localtime=time.asctime(time.localtime(time.time()))
#=========================info=====================
lblInfo = Label(Tops, font=('arial', 50, 'bold'),text="gabbi system",fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial', 20, 'bold'),text=localtime,fg="Steel Blue", bd=20, anchor='w')
lblInfo.grid(row=1,column=0)
#===========================Calculator==========================
txtDisplay = Entry(f2,font=('arial', 20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right')


root.mainloop()
