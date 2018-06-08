from tkinter import *
from tkinter import filedialog
def close():
    exit()


root = Tk()
root.title("boas truck system")
text = Label(root, text="truck business",font="times 32", width="50")
text.pack(side=TOP)

labe1 = Label(root, text="name")

menubar = Menu(root)

filemenu= Menu(menubar, tearoff=0)
filemenu.add_command(label="Close", command=close)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

root.fileName = filedialog.askopenfile(filetypes = (("boasfiles","*.hc"),("All files", "*.*") ) )

