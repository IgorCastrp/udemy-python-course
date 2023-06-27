from tkinter import *


def button_clicked():
    my_label.config(text=my_input.get())


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I'm a Label", font=("Ink Free", 30, "bold"))
my_label.config(text="New Text", padx=50, pady=50)
my_label.grid(column=0, row=0)

# Button
my_button = Button(text="Click Me", command=button_clicked)
my_button2 = Button(text="New Button", command=button_clicked)
my_button.grid(column=1, row=1)
my_button2.grid(column=2, row=0)
# Entry
my_input = Entry()
my_input.grid(column=3, row=2)




window.mainloop()
