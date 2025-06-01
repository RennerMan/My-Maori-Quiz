"""V4 of the Quiz Tracker function. Fixed score that wasn't working in V3,
as a result of clicking confirm on a correct question multiple times, which
increased the score each time without giving a new question. Also fixed error
of players with the same name getting increasingly more points. In addition to
this, also hid main popup when player details is run instead of instructions.
Now there is only 1 popup on screen at a time."""

# Import statements for tkinter, random for quiz questions
# os, as this is the only way to delete files outside of python (highscore)
from tkinter import *
from tkinter import messagebox
import random
import os


# The Maori_Quiz class. Encompasses the rest of the code to keep code simple
# And have all variables accessible to functions without the 'global' command
class MaoriQuiz:
    # Initialising base popup setup
    def __init__(self):
        self.root = Tk()
        self.root.title("Maori Quiz")
        self.root.geometry("900x600")
        self.root.configure(bg="brown1")
        self.main_popup = Label(self.root, bg="black", fg="azure",
                                text="Welcome to the \nMaori Quiz!",
                                font=("comic_sans", 50, "bold", "italic"),
                                borderwidth=3,
                                relief="solid")

        # Spiral photos. Added a flipped spiral by flipping the image
        # And incorporating it like the other one
        self.spiral = PhotoImage(
            file=r"C:\Users\jdjre\OneDrive - Middleton Grange School\2025\DTC\3.7 Programming\Assessment\Spiral.png")
        self.f_spiral = PhotoImage(
            file=r"C:\Users\jdjre\OneDrive - Middleton Grange School\2025\DTC\3.7 Programming\Assessment\Flipped_spiral.png")

        self.l_spiral = Label(self.root, image=self.spiral, bg="brown1")
        self.l_spiral.pack(side=LEFT)
        self.r_spiral = Label(self.root, image=self.f_spiral, bg="brown1")
        self.r_spiral.pack(side=RIGHT)
        self.main_popup.pack()
        # The main start button seen on the start GUI
        self.start_button = Button(
            self.root,
            text="Start",
            bg="black",
            fg="azure",
            font=("Comic Sans MS", 30, "bold"),
            command=self.player_details)
        self.start_button.pack(pady=180)

        # Variables for player data and game state
        self.name = ""
        self.score = 0
        self.quiz_no = 0
        self.highscore_file = "highscores.txt"

        # Dictionary containing Māori names for numbers 1-30
        # And their number counterparts
        self.questions = {
            "Tahi": 1, "Rua": 2, "Toru": 3, "Wha": 4, "Rima": 5, "Ono": 6,
            "Whitu": 7, "Waru": 8, "Iwa": 9, "Tekau": 10, "Tekau ma Tahi": 11,
            "Tekau ma Rua": 12, "Tekau ma Toru": 13, "Tekau ma Wha": 14,
            "Tekau ma Rima": 15, "Tekau ma Ono": 16, "Tekau ma Whitu": 17,
            "Tekau ma Waru": 18, "Tekau ma Iwa": 19, "Rua Tekau": 20,
            "Rua Tekau ma Tahi": 21, "Rua Tekau ma Rua": 22, "Rua Tekau ma "
                                                             "Toru": 23,
            "Rua Tekau ma Wha": 24, "Rua Tekau ma Rima": 25,
            "Rua Tekau ma Ono": 26,
            "Rua Tekau ma Whitu": 27, "Rua Tekau ma Waru": 28,
            "Rua Tekau ma Iwa": 29,
            "Toru Tekau": 30
        }

    # Creates standardized popup windows
    def create_popup(self, title, width=400, height=300, bg="brown1"):
        popup = Toplevel(self.root)
        popup.title(title)
        popup.geometry(f"{width}x{height}")
        popup.configure(bg=bg)
        return popup
        # Displays the instructions popup before starting the quiz

    def show_instructions(self):
        popup = self.create_popup("Instructions", 500, 300)

        Label(popup, text="Instructions", bg="black", fg="azure",
              font=("Serif", 16, "bold"), borderwidth=2, relief="solid").pack(
            pady=10)

        instr = (
            f"Welcome {self.name}!\n"
            f"You will be asked {self.quiz_no} questions.\n"
            "Select the correct number for each Maori word.\n"
            "At the end, your score will be displayed.\n"
            "Good luck!")
        Label(popup, text=instr, bg="brown1", fg="white", justify=CENTER,
              font=("Serif", 15, "bold")).pack(padx=20, pady=10)

        # The start quiz button
        Button(
            popup,
            text="Start Quiz",
            bg="black",
            fg="azure",
            font=("Comic Sans MS", 14, "bold"),
            command=lambda: [popup.destroy(), self.quiz_questions()]
        ).pack(pady=20)

    # player details function. Asks for name and no. of quiz questions
    def player_details(self):
        self.root.withdraw()
        popup = Toplevel(self.root)
        popup.geometry("400x400")
        popup.configure(bg="brown2")

        name_label = Label(popup, text="What is your name?", bg="black",
                           fg="white",
                           font=("Serif", 15, "bold"))
        name_label.pack(pady=20)

        name_entry = Entry(popup)
        name_entry.pack(pady=20)

        quiz_options = ["5", "10", "20", "30"]
        options_var = StringVar(popup)
        options_var.set("Select no. of quiz questions:")

        choices = OptionMenu(popup, options_var, *quiz_options)
        choices.configure(bg="black", fg="white", font=("Serif", 14, "bold"))
        choices.pack(pady=20)

        def confirm():
            name = name_entry.get().strip()
            num = options_var.get()

            # Splits the name given into different parts if there is a
            # space. If these parts aren't all letters of the alphabet,
            # display error msg
            if not all(part.isalpha() for part in name.split()):
                messagebox.showerror("Invalid Name",
                                     "Name must contain only letters and "
                                     "spaces.")
                return
            # validate quiz count
            if num not in quiz_options:
                messagebox.showerror("Invalid Selection",
                                     "Please choose number of questions.")
                return
            self.name = name
            self.quiz_no = int(num)
            # Reset score when starting new quiz
            self.score = 0
            popup.destroy()
            self.show_instructions()

        confirm_btn = Button(popup, text="Click to confirm", bg="black",
                             fg="white",
                             font=("Serif", 12, "bold"), borderwidth=2,
                             relief="solid",
                             command=confirm)
        confirm_btn.pack(pady=70)

    def quiz_questions(self):
        quiz_data = random.sample(list(self.questions.items()), self.quiz_no)

        def ask(index):
            if index >= self.quiz_no:
                self.show_score()
                return
            num_word, correct_answer = quiz_data[index]

            popup = Toplevel(self.root)
            popup.geometry("400x300")
            popup.configure(bg="brown1")
            quiz_length = Label(popup, text=f"Question {index + 1}",
                                bg="brown1",
                                fg="white", font=("Serif", 15, "bold"))
            quiz_length.pack()
            question_label = Label(popup,
                                   text=f"What number is '{num_word}'?",
                                   bg="brown1", fg="white",
                                   font=("Serif", 15, "bold"))
            question_label.pack(pady=20)

            all_vals = list(set(self.questions.values()) - {correct_answer})
            wrong_answers = random.sample(all_vals, 2)
            options = wrong_answers + [correct_answer]
            random.shuffle(options)

            clicked = StringVar(popup)
            clicked.set("Choose an answer")
            choice = OptionMenu(popup, clicked, *options)
            choice.configure(bg="black", fg="white",
                             font=("Serif", 12, "bold"),
                             borderwidth=2, relief="solid")
            choice.pack(pady=20)

            # Creates a list containing the 'False' value for the answer
            answered = [False]

            def confirm():
                # Checks if the only item in the answered list is True.
                # If it is, exit the function (return)
                # If not, set answered to true and continue.
                # What the 'answered' section of the code does is
                # Ensure that I can't click the confirm button for a correct
                # Question multiple times, adding more points
                # As explained at the top of my code
                if answered[0]:
                    return
                answered[0] = True

                selected = clicked.get()
                if selected == "Choose an answer":
                    messagebox.showwarning("No Selection",
                                           "Please choose an answer "
                                           "before confirming.")
                    answered[0] = False  # Resets if no selection made
                    return
                elif selected == str(correct_answer):
                    messagebox.showinfo("Result", "Correct!")
                    self.score += 1
                else:
                    messagebox.showinfo("Result",
                                        f"Incorrect! The correct answer was "
                                        f"{correct_answer}.")
                popup.destroy()
                ask(index + 1)

            confirm_btn = Button(popup, text="Click to confirm", bg="black",
                                 fg="white", font=("Serif", 12, "bold"),
                                 borderwidth=2, relief="solid",
                                 command=confirm)
            confirm_btn.pack(pady=20)

        ask(0)

    # Display final score and options for restart, quit, or view high scores
    def show_score(self):
        # Save current score to high scores file
        self.save_high_score()
        popup = self.create_popup("Final Score", 400, 400)

        # Display final score
        Label(popup,
              text=f"{self.name}, your final score is "
                   f"{self.score}/{self.quiz_no}",
              bg="black", fg="white", font=("Serif", 16, "bold")).pack(
            pady=20)

        # 'Restart', 'Quit', and 'View high scores' buttons
        Button(
            popup, text="Restart", bg="green", fg="white",
            font=("Serif", 12, "bold"),
            command=lambda: [popup.destroy(), self.player_details()]
        ).pack(pady=10)
        Button(popup, text="Quit", bg="red", fg="white",
               font=("Serif", 12, "bold"), command=self.root.quit).pack(
            pady=10)
        Button(
            popup, text="View High Scores", bg="blue", fg="white",
            font=("Serif", 12, "bold"), command=self.show_high_scores
        ).pack(pady=10)

    # Saves the current player's score to the high scores file
    def save_high_score(self):
        with open(self.highscore_file, "a") as file:
            file.write(f"{self.name}: {self.score}/{self.quiz_no}\n")

    # Display all recorded high scores in a popup window
    def show_high_scores(self):
        popup = self.create_popup("High Scores", 400, 400, "white")

        # Create title
        Label(popup, text="High Scores", font=("Serif", 16, "bold"),
              bg="black", fg="white").pack(pady=10)

        # Read and display scores from file
        if os.path.exists(self.highscore_file):
            with open(self.highscore_file, "r") as file:
                scores = file.read()
        else:
            scores = "No scores recorded yet."

        Label(popup, text=scores, font=("Serif", 12), bg="white",
              justify=LEFT).pack(padx=10, pady=10)

        # Create delete scores button
        Button(
            popup, text="Delete Scores", bg="red", fg="white",
            font=("Serif", 10, "bold"), command=self.delete_scores
        ).pack(pady=10)

    # Delete the high scores file and show confirmation message
    def delete_scores(self):
        if os.path.exists(self.highscore_file):
            os.remove(self.highscore_file)
            messagebox.showinfo("Deleted",
                                "All high scores have been deleted.")

    # A function to start the main loop. Must be done through a function
    # To ensure it is connected to the class via 'self'
    def run(self):
        self.root.mainloop()


# Sets a variable to the class, then runs the 'run' function above
# From that variable
if __name__ == "__main__":
    quiz = MaoriQuiz()
    quiz.run()
