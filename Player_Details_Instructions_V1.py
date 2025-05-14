from tkinter import *

root = Tk()
root.title("Maori Quiz")
root.geometry("900x600")

spiral = PhotoImage(file=r"C:\Users\jdjre\OneDrive - Middleton Grange "
                         r"School\2025\DTC\3.7 "
                         r"Programming\Assessment\Spiral.png")
f_spiral = PhotoImage(file=r"C:\Users\jdjre\OneDrive - Middleton Grange "
                           r"School\2025\DTC\3.7 "
                           r"Programming\Assessment\Flipped_spiral.png")
spiral_icon = Label(root, image=spiral)
spiral_icon.pack(side=LEFT)
spiral_icon2 = Label(root, image=f_spiral)
spiral_icon2.pack(side=RIGHT)

main_popup = Label(root, bg="black", fg="azure",
                   text="Welcome to the \nMaori Quiz!",
                   font=("comic_sans", 45, "bold", "italic"), borderwidth=2,
                   relief="solid")
main_popup.pack(ipadx=20)


def quiz_Questions():
    # Create a new popup window
    popup = Toplevel(root)
    popup.geometry("400x300")
    popup.configure(bg="brown1")

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


def player_details(name, age):
    ask_Name = Label(root, text="What is your name?")
    ask_Name.pack()
    ask_Age = Label(root, text="What is your age?")
    name = Entry(popup)
    age = Entry(popup)
    confirmation = Button(popup, text="Click to confirm", bg="aquamarine3",
                          fg="azure4", font=("serif", 12, "bold"),
                          borderwidth=2, relief="solid")
    confirmation.pack(pady=20)
    if confirmation:
        return name, age

if player_details(name) 
start = Button(root, bg="black", fg="azure", text="Start",
               font=("comic_sans", 30, "bold"),
               command=lambda:player_details())
start.pack(pady=200)

root.configure(bg="brown1")
root.mainloop()
