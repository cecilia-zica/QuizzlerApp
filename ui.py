from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "Italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        # - - - Window - - -
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width= 400, height= 226)
        self.window.config(padx=20 , pady=20 , bg=THEME_COLOR, highlightthickness= 0)

        # - - - Score - - -
        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            bg= THEME_COLOR, fg= "white"
        )
        self.score_label.grid(row= 0, column= 1, sticky= "e")

        # - - - Canvas - - -
        self.canvas = Canvas(width=300, height=250, bg= "white", highlightthickness=0, bd= 0)
        self.questions_txt = self.canvas.create_text(
            150, 125,
            width= 280,
            text="Question",
            font=("Ariel", 20, "italic"),
            fill= THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan= 2, sticky= "nsew", pady=50)


        # - - - Buttons - - -
        true_button_img = PhotoImage(file="images/true.png")
        false_button_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image= true_button_img, highlightthickness=0, command= self.true_pressed)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_button_img, highlightthickness=0, command= self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.questions_txt, text= q_text)
        else:
            self.canvas.itemconfig(self.questions_txt, text= "You've reached the end of the quiz.")
            self.true_button.config(state= "disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg= "red")

        self.window.after(1000, self.get_next_question)

