from tkinter import *
root = Tk()
root.title("Menu Bar")
root.geometry("240x160")


def save():
    print("File Saved Successfully")

def Open():
    print("File Opened Successfully")


menubar=Menu(root)

# creating file drop down
file = Menu(menubar, tearoff=0)  
file.add_command(label="Open",command=Open)
file.add_command(label="New Notebook") 

file.add_separator()

file.add_command(label="Make a Copy")  
file.add_command(label="Rename...")  
file.add_command(label="Save as...",command=save)  
file.add_command(label="Close",command=quit)

menubar.add_cascade(label="File", menu=file)

#creating drop down for EDIT

edit= Menu(menubar,tearoff=0) 
 
edit.add_command(label="Cut Cells")
edit.add_command(label="Copy Cells") 

edit.add_separator()

edit.add_command(label="Split Cell")  
edit.add_command(label="Move Cell Up")  
edit.add_command(label="Move Cell Down") 

menubar.add_cascade(label="Edit", menu=edit)

#creating drop down for View

view= Menu(menubar,tearoff=0) 
 
view.add_command(label="Toggle Header")
view.add_command(label="Toggle Toolbar") 

view.add_command(label="Toggle Line Numbers")  
view.add_command(label="Cell Toolbar")  

menubar.add_cascade(label="View", menu=view)

#creating drop down for Help

help= Menu(menubar,tearoff=0) 
 
help.add_command(label="Notebook Help")
help.add_command(label="Markdown") 
help.add_command(label="About")
menubar.add_cascade(label="Help",menu=help)

#here we are configuring our menu_bar to root
root.config(menu=menubar)


photo=PhotoImage(file="C:/Users/vedan/Desktop/RPOOP/tkinter1/py.png")
l1=Label(image=photo)
l1.pack()



root.mainloop()