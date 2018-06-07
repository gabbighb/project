from tkinter import *
import random
import time
import datetime

root = Tk()
root.geometry("100x600+180+20")
root.title("simple Calculator by GABRIEL")

Tops = Frame(root, width=100, height= 50, bd=16, relief="raise")
Tops.pack(side=TOP)
Tops = Frame(root, width=100, height= 50, bd=16, relief="raise")
Tops.pack(side=TOP)

inBotto1=Frame(root, width=600, height=600, bd=16, relief="raise")
inBotto1.pack(side=LEFT)

inBotto2=Frame(root, width=400, height=600, bd=16, relief="raise")
inBotto2.pack(side=RIGHT)

lblInfo =Label(Tops, font = ('Helvetica',50,'bold'), text="Gabbi Systems",
               bd=16, anchor='w')
lblInfo.grid(row=0,column=0, )

var = IntVar()
firstnum = IntVar()
secondnum = IntVar()
Total = IntVar()

rb1 = Radiobutton(inBotto1, text="adittion", variable=var, value=1,
                  font=('Helvetica',22,'bold')).grid(row=0, column=0, sticky=W)

rb2 = Radiobutton(inBotto1, text="subtraction", variable=var, value=2,
                  font=('Helvetica',22,'bold')).grid(row=0, column=0, sticky=W)

rb3 = Radiobutton(inBotto1, text="Multiplacation", variable=var, value=3,
                  font=('Helvetica',22,'bold')).grid(row=0, column=0, sticky=W)

rb4 = Radiobutton(inBotto1, text="Division", variable=var, value=4,
                  font=('Helvetica',22,'bold')).grid(row=0, column=0, sticky=W)

rb5 = Radiobutton(inBotto1, text="Modulus", variable=var, value=5,
                  font=('Helvetica',22,'bold')).grid(row=0, column=1, sticky=W)

rb6 = Radiobutton(inBotto1, text="Exponent", variable=var, value=6,
                  font=('Helvetica',22,'bold')).grid(row=1, column=1, sticky=W)

rb7 = Radiobutton(inBotto1, text="Floor Division", variable=var, value=7,
                  font=('Helvetica',22,'bold')).grid(row=2, column=1, sticky=W)

lblFirstnum = Label(inBotto1, font=('Helvetica',22,'bold'), text="Enter first Number",
                    fg="black").grid(row=4, column=0, sticky=W)

txtfirstnum = Label(inBotto1, font=('Helvetica',22,'bold'), bd=4, width=13, bg="white",
                    textvariable=firstnum).grid(row=4, column=1)

lblsecondnum = Label(inBotto1, font=('Helvetica',22,'bold'), bd=4, width=13, bg="white",
                    textvariable=firstnum).grid(row=4, column=1)









root.mainloop()
