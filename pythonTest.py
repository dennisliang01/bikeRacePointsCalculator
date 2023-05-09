from tkinter import *
from tkinter import messagebox

def show_msg():
    messagebox.showinfo("Message", "This is a test message pop up");

root = Tk()

root.title("Race Points Calculator")
root.geometry("400x200")

my_label_1 = Label(root, text = "This is a cycling points calculator program")
my_label_2 = Label(root, text = "Please enter your race history")

#my_label_1.grid(row=0, column=2)
#my_label_2.grid(row=0, column=1)
my_label_1.pack()
my_label_2.pack()

mybutton = Button(root, text = "Enter", command = show_msg)
mybutton.pack()

root.mainloop()