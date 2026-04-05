from tkinter import *

def miles_to_km():
    miles = float(milesInput.get())
    km = round(miles * 1.609, 2)
    kilometer_label_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

milesInput = Entry(width=10)
milesInput.grid(column=1, row=0)

milesText = Label(text="Miles")
milesText.grid(column=2, row=0)

is_equal_to_text = Label(text="is equal to")
is_equal_to_text.grid(column=0, row=1)

kilometer_label_result = Label(text="0")
kilometer_label_result.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

result_button = Button(text="Calculate", command=miles_to_km)
result_button.grid(column=1, row=2)

window.mainloop()