""" V1 of the score tracker component. Updated Quiz Questions with restart,
quit, final score, and high-score tracking."""

# Import statements for tkinter, random for quiz questions
# os, as this is the only way to delete additional files,
# which I decided to add
from tkinter import *
from tkinter import messagebox
import random
import os

# Base popup setup
root = Tk()
root.title("Maori Quiz")
root.geometry("900x600")
root.configure(bg="brown1")
# Spiral photos. Added a flipped spiral by flipping the image
# And incorporating it like the other one
spiral = PhotoImage(
    file=r"C:\Users\jdjre\OneDrive - Middleton Grange School\2025\DTC\3.7 Programming\Assessment\Spiral.png")
f_spiral = PhotoImage(
    file=r"C:\Users\jdjre\OneDrive - Middleton Grange School\2025\DTC\3.7 Programming\Assessment\Flipped_spiral.png")
spiral_icon = Label(root, image=spiral, bg="brown1")
spiral_icon.pack(side=LEFT)
spiral_icon2 = Label(root, image=f_spiral, bg="brown1")
spiral_icon2.pack(side=RIGHT)

# Global variables
quiz_no = 0
name = ""
score = 0
highscore_file = "highscores.txt"
# My quiz questions- Contains dictionary of maori names and actual numbers
questions = {
    "Tahi": 1, "Rua": 2, "Toru": 3, "Wha": 4, "Rima": 5, "Ono": 6,
    "Whitu": 7, "Waru": 8, "Iwa": 9, "Tekau": 10, "Tekau ma Tahi": 11,
    "Tekau ma Rua": 12, "Tekau ma Toru": 13, "Tekau ma Wha": 14,
    "Tekau ma Rima": 15, "Tekau ma Ono": 16, "Tekau ma Whitu": 17,
    "Tekau ma Waru": 18, "Tekau ma Iwa": 19, "Rua Tekau": 20,
    "Rua Tekau ma Tahi": 21, "Rua Tekau ma Rua": 22, "Rua Tekau ma Toru": 23,
    "Rua Tekau ma Wha": 24, "Rua Tekau ma Rima": 25, "Rua Tekau ma Ono": 26,
    "Rua Tekau ma Whitu": 27, "Rua Tekau ma Waru": 28, "Rua Tekau ma Iwa": 29,
    "Toru Tekau": 30
}

main_popup = Label(root, bg="black", fg="azure",
                   text="Welcome to the \nMaori Quiz!",
                   font=("Comic Sans MS", 45, "bold", "italic"),
                   borderwidth=2, relief="solid")
main_popup.pack(ipadx=20, pady=20)


# player details function. Asks for name and no. of quiz questions
def player_details():
    # popup setup
    popup = Toplevel(root)
    popup.geometry("400x400")
    popup.configure(bg="brown2")
    # Asks for name
    name_label = Label(popup, text="What is your name?", bg="black",
                       fg="white", font=("Serif", 15, "bold"))
    name_label.pack(pady=20)
    name_entry = Entry(popup)
    name_entry.pack(pady=20)
    # Number of quiz questions dropdown
    quiz_options = [5, 10, 20, 30]
    options_var = StringVar(popup)
    options_var.set("Select no. of quiz questions:")
    choices = OptionMenu(popup, options_var, *quiz_options)
    choices.configure(bg="white", fg="black", font=("Serif", 14, "bold"))
    choices.pack(pady=20)

    # confirmation of name and quiz no.
    def confirm():
        global quiz_no, name, score
        name_input = name_entry.get().strip()
        selected = options_var.get()

        if not name_input.isalpha():
            messagebox.showerror("Invalid Name",
                                 "Name must contain only letters.")
            return
        if selected not in map(str, quiz_options):
            messagebox.showerror("Invalid Selection",
                                 "Please choose number of questions.")
            return
        # Sets name to name_input and quiz_no to selected no. for later use
        name = name_input
        quiz_no = int(selected)
        score = 0
        popup.destroy()
        show_instructions()

    confirm_btn = Button(popup, text="Click to confirm", bg="black",
                         fg="white", font=("Serif", 12, "bold"),
                         borderwidth=2, relief="solid", command=confirm)
    confirm_btn.pack(pady=20)


def show_instructions():
    # popup setup
    instr_popup = Toplevel(root)
    instr_popup.geometry("500x300")
    instr_popup.configure(bg="brown1")

    instr_title = Label(instr_popup, text="Instructions", bg="black",
                        fg="azure", font=("Serif", 16, "bold"), borderwidth=2,
                        relief="solid")
    instr_title.pack(pady=10)
    # Instructions
    instr_text = (
        f"Welcome {name}!\n"
        f"You will be asked {quiz_no} questions.\n"
        "Select the correct number for each Maori word.\n"
        "At the end, your score will be displayed.\n"
        "Good luck!"
    )
    instr_label = Label(instr_popup, text=instr_text, bg="brown1",
                        fg="white", justify=CENTER,
                        font=("Serif", 15, "bold"))
    instr_label.pack(padx=20, pady=10)

    start_btn = Button(instr_popup, text="Start Quiz", bg="black", fg="azure",
                       font=("Comic Sans MS", 14, "bold"),
                       command=lambda: [instr_popup.destroy(),
                                        quiz_questions()])
    start_btn.pack(pady=20)


# Quiz questions. Asks the user what the number for a maori name is,
# Providing 3 options for them to choose from.
def quiz_questions():
    quiz_data = random.sample(list(questions.items()), quiz_no)

    def ask(index):
        if index >= quiz_no:
            return show_score()

        num_word, correct_answer = quiz_data[index]
        # Popup setup
        popup = Toplevel(root)
        popup.geometry("400x300")
        popup.configure(bg="brown1")

        question_label = Label(popup, text=f"What number is '{num_word}'?",
                               bg="brown1", fg="white",
                               font=("Serif", 15, "bold"))
        question_label.pack(pady=20)

        all_vals = list(set(questions.values()) - {correct_answer})
        wrong_answers = random.sample(all_vals, 2)
        options = wrong_answers + [correct_answer]
        random.shuffle(options)
        # Dropdown of the multichoice answers
        clicked = StringVar(popup)
        clicked.set("Choose an answer")
        choice = OptionMenu(popup, clicked, *options)
        choice.configure(bg="black", fg="white",
                         font=("Serif", 12, "bold"),
                         borderwidth=2, relief="solid")
        choice.pack(pady=20)

        # Confirmation
        def confirm():
            global score
            selected = clicked.get()
            if selected == str(correct_answer):
                score += 1
                messagebox.showinfo("Result", "Correct!")
            else:
                messagebox.showinfo(
                    "Result",
                    f"Incorrect! The correct answer was {correct_answer}.")
            popup.destroy()
            ask(index + 1)

        confirm_btn = Button(popup, text="Click to confirm", bg="black",
                             fg="white", font=("Serif", 12, "bold"),
                             borderwidth=2, relief="solid", command=confirm)
        confirm_btn.pack(pady=20)

    ask(0)


def show_score():
    save_high_score()
    # Popup setup
    popup = Toplevel(root)
    popup.geometry("400x400")
    popup.configure(bg="brown1")
    # Shows correct questions over total questions asked (eg: 9/10)
    score_label = Label(popup,
                        text=f"{name}, your final score is {score}/{quiz_no}",
                        bg="black", fg="white", font=("Serif", 16, "bold"))
    score_label.pack(pady=20)
    # Restarts the program
    Button(popup, text="Restart", bg="green", fg="white",
           font=("Serif", 12, "bold"),
           command=lambda: [popup.destroy(), player_details()]).pack(pady=10)
    # Quits the program
    Button(popup, text="Quit", bg="red", fg="white",
           font=("Serif", 12, "bold"), command=root.quit).pack(pady=10)
    # Allows user to see the high scores
    Button(popup, text="View High Scores", bg="blue", fg="white",
           font=("Serif", 12, "bold"), command=show_high_scores).pack(pady=10)


def save_high_score():
    with open(highscore_file, "a") as file:
        file.write(f"{name}: {score}/{quiz_no}\n")


def show_high_scores():
    # Popup setup
    popup = Toplevel(root)
    popup.geometry("400x400")
    popup.configure(bg="white")
    # High scores title
    title = Label(popup, text="High Scores", font=("Serif", 16, "bold"),
                  bg="black", fg="white")
    title.pack(pady=10)
    # If there are any highscores, then show them. Else, say there is none.
    if os.path.exists(highscore_file):
        with open(highscore_file, "r") as file:
            scores = file.read()
    else:
        scores = "No scores recorded yet."
    # The label for the scores
    score_label = Label(popup, text=scores, font=("Serif", 12), bg="white",
                        justify=LEFT)
    score_label.pack(padx=10, pady=10)
    # Deletes all high scores
    Button(popup, text="Delete Scores", bg="red", fg="white",
           font=("Serif", 10, "bold"), command=delete_scores).pack(pady=10)


def delete_scores():
    if os.path.exists(highscore_file):
        os.remove(highscore_file)
        messagebox.showinfo("Deleted", "All high scores have been deleted.")


# Start button on main popup that begins the program
start = Button(root, text="Start", bg="black", fg="azure",
               font=("Comic Sans MS", 30, "bold"), command=player_details)
start.pack(pady=100)

root.mainloop()
