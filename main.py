# Creates the application window
import JSONmaker as jm
import tkinter as tk
from pathlib import Path
import json

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
    initialize_data()
    print(food_journal)
    add_food(entry_food.get(), entry_date.get(), entry_time.get(), entry_calories.get())
    print(food_journal)
    write_json('food_journal', food_journal)
    clear_entry()


# Reads in the Json files and turn them into arrays/dictionaries to be used
def initialize_data():
    global food_journal
    global food_cal
    if Path('food_journal.json').is_file():
        food_journal = read_json('food_journal')
    else:
        write_json('food_journal', {})
    if Path('food_cal.json').is_file():
        food_cal = read_json('food_cal')
    else:
        write_json('food_cal', {})


# Function to add the food eaten on the specific date, specific time and calories
def add_food(food, date, time, calorie):
    if date not in food_journal:
        food_journal[date] = []
        temp_food_dict = {
            'name': food,
            'time': time,
            'calories': calorie}
        food_journal[date].append(temp_food_dict)
    else:
        temp_food_dict = {
            'name': food,
            'time': time,
            'calories': calorie}
        food_journal[date].append(temp_food_dict)


# Function to add any food from the food_journal to a dictionary of food and their calories
def add_food_cal(food, calorie):
    if food not in food_cal:
        food_cal[food] = calorie


# This saves the created dictionary in a json text file
def write_json(name, array):
    with open(name + '.json', 'w') as outfile:
        json.dump(array, outfile)


# This reads the created dictionary from a json text file (Currently prints in console)
def read_json(name):
    with open(name + '.json') as json_file:
        data = json.load(json_file)
        return data


# Loops through all the food_journal entries and extract the names and calories into food_cal
def fill_food_cal():
    for array in food_journal:
        for entry in food_journal[array]:
            food = entry['name']
            calorie = entry['calories']
            add_food_cal(food, calorie)
    write_json('food_cal', food_cal)


# Loops through all food_journal entries and sees whether the calories in them
# are 0, if so then it searches in food_cal for the right calories and inserts it back
def complete_food_journal():
    for array in food_journal:
        for entry in food_journal[array]:
            food = entry['name']
            calorie = entry['calories']
            if calorie == 0:
                # print(food_journal[calorie])
                # print(food_cal[food])
                entry['calories'] = food_cal[food]
    write_json('food_journal', food_journal)


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
