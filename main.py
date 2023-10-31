#Tkinter is for the design of graphical interfaces.

import tkinter


#window

window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=500, height=400)


#Label is to display text to the user:

my_label = tkinter.Label(text = "label", font=("Arial", 25, "normal"))
my_label.config(bg="black", fg="white")
#my_label.pack()
#my_label.pack(side = "right")  #right or top, bottom, left
#my_label.place(x=0, y=0)
my_label.grid(row=0, column=0)

#There must be at least one of "pack", "place" ->
#-> and "grid" so that the widgets appear on the screen.

#The grid divides the screen into 3 rows and 3 columns ->
#-> and places the widgets according to x and y values.


def click_button():
    #print("button clicked")
    user_input = my_entry.get()  #to print the text ->
    print(user_input)  #-> entered in the entry

#Button is for typing the text by clicking:

my_button = tkinter.Button(text="button", command=click_button)
#my_button.pack()
#my_button.pack(side = "right")
#my_button.place(x=225-23.5, y=200-13)
#my_button.update()
#print(my_button.winfo_height())
#print(my_button.winfo_width())
my_button.grid(row=1, column=1)

#Search: tkinter get widget height

#To place the widget in the middle of the screen, ->
#-> we find the width and height of the widget and ->
#-> subtract half of it from half the width and ->
#-> height of the screen.


#Entry opens a space for writing text:

my_entry = tkinter.Entry(width=30)
#my_entry.pack()
#my_entry.pack(side = "right")
#my_entry.place(x=100, y=100)
my_entry.grid(row=2, column=2)


window.mainloop()