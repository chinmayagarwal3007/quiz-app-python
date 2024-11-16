from question_data import question_data
from tkinter import * 
import random
import html

questions_list = question_data

current_question = ""
current_answer = ""
question_remaining = 30

def generate_ques():
    global current_answer, question_remaining
    current_data = random.choice(questions_list)
    current_question = html.unescape(current_data["question"])
    current_answer = current_data["correct_answer"]
    questions_list.remove(current_data)
    question_remaining -= 1
    question_left["text"] = f"Questions Left: {question_remaining}/30"
    question["text"] = current_question



score = 0

def when_right():
    global score
    if(current_answer == "True"):
        score += 1
        scorecard["text"] = f"score: {score}"
    generate_ques()
        

def when_wrong():
    global score
    if(current_answer == "False"):
        score += 1
        scorecard["text"] = f"score: {score}"
    generate_ques()



window = Tk()
window.title("Quiz App")
window.config(padx = 50, pady = 50)

question_left = Label(text=f"Questions Left: {question_remaining}/30")
question_left.grid(row= 0, column=1)
question_left.config(padx=20, pady=20)


scorecard = Label(text=f"Score: {score}")
scorecard.grid(row=0, column=0)
scorecard.config(padx=20, pady=20)

question = Label(text=current_question)
question.grid(row=1, column=0,columnspan=2, sticky="EW")
question.config(padx=20, pady=20)

yes_button = Button(text="Yes", command=when_right)
yes_button.grid(row=2, column=0)
yes_button.config(padx=5, pady=5)

no_button = Button(text="No", command=when_wrong)
no_button.grid(row=2, column=1)
no_button.config(padx=5, pady=5)

generate_ques()

window.mainloop()

