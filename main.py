# Creates the application window
import JSONmaker as jm
import tkinter as tk

# food_journal is an array containing the food journal entries
# food_dictionary is a dictionary of foods and their calories
food_journal = {}
food_cal = {}


def clear_entry():
    entry_date.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    entry_food.delete(0, tk.END)
    entry_calories.delete(0, tk.END)


def submit_entry():
    jm.initialize_data()
    jm.add_food(entry_food.get(), entry_date.get(), entry_time.get(), entry_calories.get())
    # jm.write_json('food_journal', food_journal)
    clear_entry()


window = tk.Tk()
window.title('Food Journal')

mainFrame = tk.Frame()
mainFrame.pack(ipadx=50, ipady=50)

label_date = tk.Label(master=mainFrame, text="Date :")
label_date.grid(row=0, column=0)
entry_date = tk.Entry(master=mainFrame)
entry_date.grid(row=0, column=1)

label_time = tk.Label(master=mainFrame, text="Time :")
label_time.grid(row=1, column=0)
entry_time = tk.Entry(master=mainFrame)
entry_time.grid(row=1, column=1)

label_food = tk.Label(master=mainFrame, text="Food :")
label_food.grid(row=2, column=0)
entry_food = tk.Entry(master=mainFrame)
entry_food.grid(row=2, column=1)

label_calories = tk.Label(master=mainFrame, text="Calories :")
label_calories.grid(row=3, column=0)
entry_calories = tk.Entry(master=mainFrame)
entry_calories.grid(row=3, column=1)

buttonFrame = tk.Frame()
buttonFrame.pack()

btn_submit = tk.Button(master=buttonFrame, text="Submit", command=submit_entry)
btn_submit.pack(side=tk.RIGHT)

btn_clear = tk.Button(master=buttonFrame, text="Clear", command=clear_entry)
btn_clear.pack(side=tk.RIGHT)

window.mainloop()
