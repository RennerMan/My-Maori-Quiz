from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Maori Quiz")
root.geometry("900x600")
root.configure(bg="brown1")

# Load and display images
spiral = PhotoImage(
    file=r"C:\Users\jdjre\OneDrive - Middleton Grange School\2025\DTC\3.7 Programming\Assessment\Spiral.png")
f_spiral = PhotoImage(
    file=r"C:\Users\jdjre\OneDrive - Middleton Grange School\2025\DTC\3.7 Programming\Assessment\Flipped_spiral.png")
spiral_icon = Label(root, image=spiral, bg="brown1")
spiral_icon.pack(side=LEFT)
spiral_icon2 = Label(root, image=f_spiral, bg="brown1")
spiral_icon2.pack(side=RIGHT)

# Welcome message
main_popup = Label(root, bg="black", fg="azure",
                   text="Welcome to the \nMaori Quiz!",
                   font=("Comic Sans MS", 45, "bold", "italic"),
                   borderwidth=2, relief="solid")
main_popup.pack(ipadx=20, pady=20)


# Function for quiz questions (placeholder)
def quiz_questions():
    popup = Toplevel(root)
    popup.geometry("400x300")
    popup.configure(bg="brown1")

    options = ["rand1", "rand2", "Correct"]
    clicked = StringVar(popup)
    clicked.set("What number is 'Correct'?: ")
    choice = OptionMenu(popup, clicked, *options)
    choice.configure(bg="aquamarine3", fg="azure4",
                     font=("Serif", 12, "bold"), borderwidth=2,
                     relief="solid")
    choice.pack(pady=20)

    confirmation = Button(popup, text="Click to confirm",
                          bg="aquamarine3", fg="azure4",
                          font=("Serif", 12, "bold"),
                          borderwidth=2, relief="solid",
                          command=lambda: messagebox.showinfo("Selected",
                                                              clicked.get()))
    confirmation.pack(pady=20)


# Function to collect player details
def player_details():
    popup = Toplevel(root)
    popup.geometry("400x300")
    popup.configure(bg="brown1")

    name_label = Label(popup, text="What is your name?", bg="brown1",
                       fg="azure4")
    name_label.pack()
    name_entry = Entry(popup)
    name_entry.pack()
    quiz_options = ["5", "10", "20", "30"]
    options_var = StringVar(popup)
    options_var.set("How many questions should there be in the quiz?")
    choices = OptionMenu(popup, options_var, *quiz_options)
    choices.configure(bg="aquamarine3", fg="azure4",
                      font=("Serif", 12, "bold"), borderwidth=2,
                      relief="solid")
    choices.pack(pady=20)

    def confirm():
        name = name_entry.get().strip()
        num = options_var.get()
        # validate name
        if not name.isalpha():
            messagebox.showerror("Invalid Name",
                                 "Name must contain only letters.")
            return
        # validate quiz count
        if num not in quiz_options:
            messagebox.showerror("Invalid Selection",
                                 "Please choose number of questions.")
            return
        popup.destroy()
        show_instructions(name, int(num))

    confirm_btn = Button(popup, text="Click to confirm", bg="aquamarine3",
                         fg="azure4", font=("Serif", 12, "bold"),
                         borderwidth=2, relief="solid", command=confirm)
    confirm_btn.pack(pady=20)


# Function to show instructions
def show_instructions(name, quiz_no):
    instr_popup = Toplevel(root)
    instr_popup.geometry("500x300")
    instr_popup.configure(bg="brown1")

    instr_title = Label(instr_popup, text="Instructions", bg="brown1",
                        fg="azure",
                        font=("Serif", 16, "bold"))
    instr_title.pack(pady=10)

    instr_text = (
        f"Welcome {name}!\n"
        f"You will be asked {quiz_no} questions.\n"
        "Select the correct Maori name for each number.\n"
        "At the end, your scores will be counted up and you have the option "
        "to try again or post your high score for others to see.\n"
        "Good luck!"
    )
    instr_label = Label(instr_popup, text=instr_text, bg="brown1",
                        fg="azure4",
                        justify=LEFT, font=("Serif", 12))
    instr_label.pack(padx=20, pady=10)

    start_btn = Button(instr_popup, text="Start Quiz", bg="black", fg="azure",
                       font=("Comic Sans MS", 14, "bold"),
                       command=quiz_questions)
    start_btn.pack(pady=20)


# Start button on main window
start = Button(root, text="Start", bg="black", fg="azure",
               font=("Comic Sans MS", 30, "bold"), command=player_details)
start.pack(pady=100)

root.mainloop()
