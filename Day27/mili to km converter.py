from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.689
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=10, pady=10)

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column= 2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()