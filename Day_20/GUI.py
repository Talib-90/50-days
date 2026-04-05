from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.title("GUI Program")
window.config(padx=20, pady=20)

# Label
label = Label(text="label", font=("Ariel", 24, "bold"))
# label.pack()
# label["text"] = "new text"
# label.config(text="new text")
label.grid(column=0,row=0)
label.config(padx=10, pady=10)

def clickMe():
    print("Click me")
    newText = input.get()
    label.config(text=newText)

button = Button(text="Button", command=clickMe)
# button.pack()
button.grid(column=1, row=1)

newButton = Button(text="new button")
newButton.grid(column=2, row=0)

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)





window.mainloop()