# Creates the application window
import JSONmaker as jm
import tkinter as tk
# food_journal is an array containing the food journal entries
# food_dictionary is a dictionary of foods and their calories
food_journal = {}
food_cal = {}
#TODO: Address the global versus local copies (between main and JSONmaker.py)


#Code review on param --> Self and master usage
class Main1:
    def __init__(self, master):
        self.master = master
        self.main_frame = tk.Frame(self.master)
        self.master.title('Food Journal')
        self.main_frame.pack(ipadx=50, ipady=50)

        # Button that when pressed creates and opens a new class/window 
        # self.button1 = tk.Button(self.main_frame, text = 'New Window', width = 25, command = self.display_data)
        # self.button1.pack()


        label_date = tk.Label(self.main_frame, text="Date :")
        label_date.grid(row=0, column=0)
        self.entry_date = tk.Entry(self.main_frame)
        self.entry_date.grid(row=0, column=1)

        label_time = tk.Label(master=self.main_frame, text="Time :")
        label_time.grid(row=1, column=0)
        self.entry_time = tk.Entry(master=self.main_frame)
        self.entry_time.grid(row=1, column=1)

        label_food = tk.Label(master=self.main_frame, text="Food :")
        label_food.grid(row=2, column=0)
        self.entry_food = tk.Entry(master=self.main_frame)
        self.entry_food.grid(row=2, column=1)

        label_calories = tk.Label(master=self.main_frame, text="Calories :")
        label_calories.grid(row=3, column=0)
        self.entry_calories = tk.Entry(master=self.main_frame)
        self.entry_calories.grid(row=3, column=1)

        buttonFrame = tk.Frame()
        buttonFrame.pack()

        self.btn_submit = tk.Button(buttonFrame, text="Submit", command=self.submit_entry) #in case its needed (command=lambda : self.submit_entry(entry_date.get(), entry_time.get(), entry_food.get(), entry_calories.get())
        self.btn_submit.pack(side=tk.RIGHT)

        self.btn_clear = tk.Button(master=buttonFrame, text="Clear", command=self.clear_entry)
        self.btn_clear.pack(side=tk.RIGHT)



    def clear_entry(self):
        self.entry_date.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.entry_food.delete(0, tk.END)
        self.entry_calories.delete(0, tk.END)


    def submit_entry(self): #coressponding to comment about lamda --> add params date, time, food, calories
        jm.initialize_data()
        temp = jm.add_food(self.entry_date.get(), self.entry_time.get(), self.entry_food.get(), self.entry_calories.get())
        print(temp)
        jm.write_json('food_journal', food_journal)
        self.clear_entry()

    # def display_data(self):
    #         self.newWindow = tk.Toplevel(self.master)
    #         self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()
        
def main():
    root = tk.Tk()
    app = Main1(root)
    root.mainloop()

if __name__ == '__main__':
    main()