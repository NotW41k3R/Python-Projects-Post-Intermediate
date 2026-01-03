from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz= quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score=Label(text="Score:0/0",font=("Ariel", 15, "italic"),fg='white', bg=THEME_COLOR, highlightthickness=0)
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250,bg="white")
        self.current_question = self.canvas.create_text(150, 125, text="Question", font=("Ariel", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        self.check_image = PhotoImage(file="images/true.png")
        self.known_button = Button(image=self.check_image, highlightthickness=0,command=lambda: self.call_check_answer("True"))
        self.known_button.grid(row=2, column=0, padx=15)

        self.cross_image = PhotoImage(file="images/false.png")
        self.unknown_button = Button(image=self.cross_image, highlightthickness=0,command=lambda: self.call_check_answer("False"))
        self.unknown_button.grid(row=2, column=1, padx=15)

        self.call_next_question()

        self.window.mainloop()

    def call_next_question(self):
        if self.quiz.still_has_questions():
            ques_text = self.quiz.next_question()
            self.canvas.itemconfig(self.current_question, text=ques_text)
        else:
            self.canvas.itemconfig(self.current_question, text="You've completed the quiz")
            self.known_button.config(state="disabled")
            self.unknown_button.config(state="disabled")

    def call_check_answer(self,answer):
        result = self.quiz.check_answer(answer)
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if result:
            self.canvas.config(bg="green")
            self.canvas.after(700, lambda: self.canvas.config(bg="white"))
        else:
            self.canvas.config(bg="red")
            self.canvas.after(700, lambda: self.canvas.config(bg="white"))

        self.canvas.after(700, self.call_next_question)
