import tkinter
from tkinter import *

root = Tk()
root.title("Maori Quiz")
root.geometry("900x600")

spiral = tkinter.PhotoImage(file=r"C:\Users\jdjre\OneDrive - Middleton Grange"
                                 r"School\2025\DTC\3.7 "
                                 r"Programming\Assessment\Spiral.png")

f_spiral = tkinter.PhotoImage(file=r"C:\Users\jdjre\OneDrive - Middleton "
                                   r"Grange"
                                   r"School\2025\DTC\3.7 "
                                   r"Programming\Assessment\Flipped_spiral"
                                   r".png")
spiral_icon = Label(root, image=spiral)
spiral_icon.pack(side=LEFT)
spiral_icon2 = Label(root, image=f_spiral)
spiral_icon2.pack(side=RIGHT)

main_popup = Label(root, bg="black", fg="azure",
                   text="Welcome to the \nMaori Quiz!",
                   font=("comic_sans", 45, "bold", "italic"), borderwidth=2,
                   relief="solid")
main_popup.pack(ipadx=20)

start = Button(root, bg="black", fg="azure", text="Start",
               font=("comic_sans", 30, "bold"))
start.pack(pady=200)


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


root.configure(bg="brown1")
root.mainloop()
