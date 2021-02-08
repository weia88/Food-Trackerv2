# Program that reads in JSON format Food_journal
# Writes a dictionary of foods and their calories
# Configures the Food_journal by adding calorie values to entries without them

import json
from pathlib import Path

# food_journal is an array containing the food journal entries
# food_dictionary is a dictionary of foods and their calories
food_journal = {}
cal_dictionary = {}


# TODO: Address the global versus local copies (between main and JSONmaker.py)


# Reads in the Json files and turn them into arrays/dictionaries to be used
def initialize_data():
    global food_journal
    if Path('food_journal.json').is_file():
        read_json('food_journal')
        print(food_journal)
    else:
        write_json('food_journal', {})
        print('not read')

    # if Path('cal_dictionary.json').is_file():
    #     cal_dictionary = read_json('cal_dictionary')
    # else:
    #     write_json('cal_dictionary', {})


# Function to add the food eaten on the specific date, specific time and calories
def add_food(date, time, food, calorie):
    if date not in food_journal:
        food_journal[date] = [{
            'name': food,
            'time': time,
            'calories': calorie}
        ]
    else:
        temp_food_dict = {
            'name': food,
            'time': time,
            'calories': calorie}
        food_journal[date].append(temp_food_dict)
    write_json('food_journal', food_journal)


# TODO: Add the proper return value

# Function to add any food from the food_journal to a dictionary of food and their calories
def add_cal_dictionary(food, calorie):
    if food not in cal_dictionary:
        cal_dictionary[food] = calorie


# This saves the created dictionary in a json text file
def write_json(name, array):
    with open(name + '.json', 'w') as outfile:
        json.dump(array, outfile)


# This reads the created dictionary from a json text file (Currently prints in console)
def read_json(name):
    global food_journal
    with open(name + '.json') as json_file:
        food_journal = json.load(json_file)
        return food_journal


# Loops through all the food_journal entries and extract the names and calories into cal_dictionary
def fill_cal_dictionary():
    for array in food_journal:
        for entry in food_journal[array]:
            food = entry['name']
            calorie = entry['calories']
            add_cal_dictionary(food, calorie)
    write_json('cal_dictionary', cal_dictionary)


# Loops through all food_journal entries and sees whether the calories in them
# are 0, if so then it searches in cal_dictionary for the right calories and inserts it back
def complete_food_journal():
    for array in food_journal:
        for entry in food_journal[array]:
            food = entry['name']
            calorie = entry['calories']
            if calorie == 0:
                # print(food_journal[calorie])
                # print(cal_dictionary[food])
                entry['calories'] = cal_dictionary[food]
    write_json('food_journal', food_journal)

# if __name__ == '__main__':
# initialize_data()
# fill_cal_dictionary()
# complete_food_journal()
