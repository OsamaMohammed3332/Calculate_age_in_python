from tkinter import *
from tkinter import messagebox

age_app = Tk()

age_app.title("OS Age App")

age_app.geometry("400x300")

text = Label(age_app, text="Write Your Age", height="2", font=("Arial", 20))
text.pack()
age = StringVar()
age.set("00")
age_input = Entry(age_app, width=2, font=("Arial", 30), textvariable=age)
age_input.pack()


def calc():
    the_age_value = age.get()
    months = int(the_age_value) * 12
    weeks = int(months) * 4
    days = int(the_age_value) * 365
    line_one = f"Your Age In Months Is ={months}"
    line_two = f"Your Age In Weeks Is ={weeks}"
    line_three = f"Your Age In Days Is ={days}"
    all_lines = [line_one, line_two, line_three]
    messagebox.showinfo("Your Age In All Time Units", "\n".join(all_lines))


bt = Button(age_app, text="Calculate Your Age", width=20,
            height=2, bg="red", fg="White", borderwidth=0, font=("Arial", 10),
            command=calc)
bt.pack()

age_app.mainloop()
