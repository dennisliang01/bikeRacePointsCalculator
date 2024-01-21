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
root.geometry("1000x500")
root.config(bg = "grey")

# Create Frame Widget
left_frame = Frame(root, width = 1000, height = 100)
left_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

#right_frame = Frame(root, width = 500, height = 100, bg = "red")
#right_frame.grid(row = 0, column = 0, padx = 10, pady = 10)


my_label_1 = Label(left_frame, text = "This is a cycling points calculator program")
my_label_1.pack(side = RIGHT)
'''
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
'''

root.mainloop()