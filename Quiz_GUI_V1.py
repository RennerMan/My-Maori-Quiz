from tkinter import *

root = Tk()
root.title("Maori Quiz")
root.geometry("800x500")

main_popup = Label(root, bg="aquamarine3", fg="azure4",
                   text="Welcome to the \nMaori Quiz!",
                   font=("serif", 50, "bold"), borderwidth=5,
                   relief="solid")
main_popup.pack(ipadx=20)


def additional_popup(action):
    # Create a new popup window
    popup = Toplevel(root)
    popup.title(f"{action}")
    popup.geometry("400x300")
    popup.configure(bg="mediumpurple1")

    # Dropdown menu
    options = ["rand1", "rand2", "Correct"]
    clicked = StringVar()
    clicked.set("What number is 'Correct'?: ")
    choice = OptionMenu(popup, clicked, *options)
    choice.configure(bg="aquamarine3", fg="azure4",
                     font=("serif", 12, "bold"), borderwidth=2,
                     relief="solid")
    choice.pack(pady=20)

    # Confirmation button
    confirmation = Button(popup, text="Click to confirm", bg="aquamarine3",
                          fg="azure4", font=("serif", 12, "bold"),
                          borderwidth=2, relief="solid")
    confirmation.pack(pady=20)


root.configure(bg="mediumpurple1")
root.mainloop()
