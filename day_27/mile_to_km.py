from tkinter import *


def calculate_converter():
    number_miles = float(my_entry.get())
    number_km = number_miles * 1.609
    km_value.config(text=f"{number_km:.4f}")


window = Tk()
window.minsize(width=300, height=200)
window.title("Mile to KM Converter")
window.config(padx=50, pady=50)

# Labels
miles = Label()
miles.config(text="Miles", padx=2)
miles.grid(column=2, row=0)

equal = Label()
equal.config(text="is equal to")
equal.grid(column=0, row=1)

km = Label()
km.config(text="Km", padx=2)
km.grid(column=2, row=1)

km_value = Label()
km_value.config(text="0")
km_value.grid(column=1, row=1)


# Entry
my_entry = Entry()
my_entry.config(width=10)
my_entry.grid(column=1, row=0)

# Button

calculate_button = Button()
calculate_button.config(text="Calculate", command=calculate_converter)
calculate_button.grid(column=1, row=2)










window.mainloop()
