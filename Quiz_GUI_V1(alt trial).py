from tkinter import *

root = Tk()
root.title("Maori Quiz")
root.geometry("900x600")

spiral = PhotoImage(file=r"C:\Users\jdjre\OneDrive - Middleton Grange "
                         r"School\2025\DTC\3.7 "
                         r"Programming\Assessment\Spiral.png")
spiral_icon = Label(root, image=spiral)
spiral_icon.pack(side=LEFT)
spiral_icon2 = Label(root, image=spiral)
spiral_icon2.pack(side=RIGHT)

main_popup = Label(root, bg="black", fg="azure",
                   text="Welcome to the \nMaori Quiz!",
                   font=("comic_sans", 45, "bold", "italic"), borderwidth=2,
                   relief="solid")
main_popup.pack(ipadx=20)

start = Button(root, bg="black", fg="azure", text="Start",
               font=("comic_sans", 30, "bold"))
start.pack(pady=200)
root.configure(bg="brown1")
root.mainloop()
