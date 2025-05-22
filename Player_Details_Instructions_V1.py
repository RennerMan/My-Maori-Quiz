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


# Function to show instructions
def show_instructions(name, quiz_no):
    # popup setup
    instr_popup = Toplevel(root)
    instr_popup.geometry("500x300")
    instr_popup.configure(bg="brown1")

    instr_title = Label(instr_popup, text="Instructions", bg="black",
                        fg="azure",
                        font=("Serif", 16, "bold"), borderwidth=2,
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

    instr_label = Label(instr_popup, text=instr_text, bg="brown1", fg="white",
                        justify=CENTER, font=("Serif", 15, "bold"))
    instr_label.pack(padx=20, pady=10)

    start_btn = Button(instr_popup, text="Start Quiz", bg="black", fg="azure",
                       font=("Comic Sans MS", 14, "bold"))
    start_btn.pack(pady=20)


# Function to collect player details
def player_details():
    popup = Toplevel(root)
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

    confirm_btn = Button(popup, text="Click to confirm", bg="black",
                         fg="white",
                         font=("Serif", 12, "bold"), borderwidth=2,
                         relief="solid",
                         command=confirm)
    confirm_btn.pack(pady=70)


# Start button on main window
start = Button(root, text="Start", bg="black", fg="azure",
               font=("Comic Sans MS", 30, "bold"), command=player_details)
start.pack(pady=100)

root.mainloop()
