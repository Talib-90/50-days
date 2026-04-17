from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.questions_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Something write here",
            font=("Ariel", 12, "bold"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=1, columnspan=2, pady=50)

        trueImage = PhotoImage(file="images/true.png")
        self.true_button = Button(image=trueImage, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column=1, row=2)

        falseImage = PhotoImage(file="images/false.png")
        self.false_button = Button(image=falseImage, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(column=2, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions_text, text=q_text)
        else:
            self.canvas.itemconfig(self.questions_text, text="You have reached the end of the question.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, isRight):
        if isRight:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

