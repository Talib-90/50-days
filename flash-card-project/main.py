from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient="records")


def nextCard():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    frenchCard = current_card["French"]
    canvas.itemconfig(create_title, text="French", fill="black")
    canvas.itemconfig(create_word, text=frenchCard, fill="black")
    canvas.itemconfig(card_background, image=front_card_img)
    flip_timer = window.after(3000, func=flipCard)


def flipCard():
    canvas.itemconfig(create_title, text="English", fill="white")
    canvas.itemconfig(create_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    nextCard()


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flipCard)

canvas = Canvas(width=800, height=526)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_card_img)
create_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
create_word = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=nextCard)
cross_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
right_button = Button(image=check_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

nextCard()

window.mainloop()
