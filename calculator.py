from tkinter import *

window = Tk()
window.geometry("316x334")  # window size
window.title("Calculator")


input_text = StringVar()
# display frame
input_frame = Frame(window, width=310, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

# input field to display the number and output
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# frame for buttons to be displayed
btns_frame = Frame(window, width=312, height=272.5, bg="grey")
btns_frame.pack()

# buttons
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
zoro = Button(btns_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
multiplication = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
division = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
substraction = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
add = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")
equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2")

# buttons alignment
seven.grid(row=0, column=0)
eight.grid(row=0, column=1)
nine.grid(row=0, column=2)
division.grid(row=0,column=3)
four.grid(row=1, column=0)
five.grid(row=1, column=1)
six.grid(row=1, column=2)
multiplication.grid(row=1,column=3)
one.grid(row=2, column=0)
two.grid(row=2, column=1)
three.grid(row=2, column=2)
substraction.grid(row=2,column=3)
zoro.grid(row=3, column=1)
equals.grid(row=3,column=2)
add.grid(row=3,column=3)


window.mainloop()
