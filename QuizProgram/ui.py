from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        #Label
        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        #Canva
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     width= 280,
                                                     font= ("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons :
        img_correct = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=img_correct, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(row=2, column=0)

        img_incorrect = PhotoImage(file="images/false.png")
        self.incorrect_button = Button(image=img_incorrect, highlightthickness=0, command=self.false_pressed)
        self.incorrect_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")
        self.canvas.config(bg="white")


    def true_pressed(self):
        check_ans = self.quiz.check_answer("True")
        self.give_feedback(check_ans)

    def false_pressed(self):
        check_ans = self.quiz.check_answer("False")
        self.give_feedback(check_ans)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)