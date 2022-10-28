# import tkinter
# from turtle import width

# window = tkinter.Tk()
# window.title("First GUI Program")
# window.minsize(width=500, height=400)

# # # Label
# my_label = tkinter.Label(text="First Lable", font=("Ariel", 20, "bold"))
# my_label.pack(side="top")

# # Placing the different text
# # my_label["text"] = "New New"
# # my_label.config(text="new")
# # my_label.pack(expand=True)


# # Buttons
# def button_clicked():
#     new_text = input.get()
#     my_label.config(text=new_text)

# button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()

# # Enter from the user
# input = tkinter.Entry()
# input.pack()
# # print(input.get())

# window.mainloop()



# Tkinter Layout Manager - pack(), place(), grid()


from tkinter import *

window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=400)
window.config(padx=10, pady=10)

# place()
my_label = Label(text="place layout manager")
my_label.place(x=50, y=10)

# pack()
# my_label = Label(text="pack layout manager")
# my_label.pack(side="top")


# grid()
# my_label = Label(text="grid layout manager")
# my_label.grid(column=3, row=4)

# my_label1 = Label(text="grid layout manager 1")
# my_label1.grid(column=2, row=2)

window.mainloop()