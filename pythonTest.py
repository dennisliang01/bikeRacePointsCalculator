from tkinter import *
from tkinter import messagebox

def show_msg():
    message_label = Label(root, 
        text = "You have clicked a button", 
        fg='#ff2f00')
    message_label.pack() 
    
def clickMe():
    clickMeLabel = Label(root, text = 'Hello ' + entryField1.get())
    clickMeLabel.pack()
    
root = Tk()

root.title("Race Points Calculator")
root.geometry("400x200")

my_label_1 = Label(root, text = "This is a cycling points calculator program")
my_label_1.pack()
my_label_2 = Label(root, text = "Please enter your race history")
my_label_2.pack()

entryField1 = Entry(root, width = 50)
entryField1.pack()

mybutton = Button(root, 
    text = "Enter",
    command = clickMe,
    padx = 30,
    pady = 30)
mybutton.pack()

root.mainloop()