# TODO: Need to restructure python comments to follow python guidelines and docstrings
import JSONmaker as jm
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# Code review on param --> Self and master usage
class StartPage:
    def __init__(self, master):
        jm.initialize_data()

        self.master = master
        self.master.title('Food Journal Home Page')
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(ipadx=50, ipady=50)

        label_date = tk.Label(self.main_frame, text="Date :")
        label_date.grid(row=0, column=0)
        self.entry_date = tk.Entry(self.main_frame)
        self.entry_date.insert(0, datetime.today().strftime("%m/%d/%Y"))
        self.entry_date.grid(row=0, column=1)
        label_date_format = tk.Label(self.main_frame, text="MM/DD/YYYY")
        label_date_format.grid(row=0, column=2)

        label_time = tk.Label(master=self.main_frame, text="Time :")
        label_time.grid(row=1, column=0)
        self.entry_time = tk.Entry(master=self.main_frame)
        self.entry_time.insert(0, datetime.now().time().strftime("%H:%M"))
        self.entry_time.grid(row=1, column=1)
        label_time_format = tk.Label(self.main_frame, text="24 Hours")
        label_time_format.grid(row=1, column=2)

        label_food = tk.Label(master=self.main_frame, text="Food :")
        label_food.grid(row=2, column=0)
        self.entry_food = tk.Entry(master=self.main_frame)
        self.entry_food.grid(row=2, column=1)

        label_calories = tk.Label(master=self.main_frame, text="Calories :")
        label_calories.grid(row=3, column=0)
        self.entry_calories = tk.Entry(master=self.main_frame)
        self.entry_calories.grid(row=3, column=1)

        self.button_frames = tk.Frame()
        self.button_frames.pack()

        # Button that when pressed creates and opens a new class/window
        self.btn_display = tk.Button(self.button_frames, text='Display Journal', width=20, bg='lightblue',
                                     command=self.display_data)
        self.btn_display.pack()

        self.btn_submit = tk.Button(self.button_frames, text="Submit", width=10,
                                    command=self.submit_entry)  # in case its needed (command=lambda : self.submit_entry(entry_date.get(), entry_time.get(), entry_food.get(), entry_calories.get())
        self.btn_submit.pack(side=tk.RIGHT)

        self.btn_clear = tk.Button(self.button_frames, text="Clear", width=10, command=self.clear_entry)
        self.btn_clear.pack(side=tk.RIGHT)

        self.btn_quit = tk.Button(self.button_frames, text="Quit", width=10, command=self.close_windows)
        self.btn_quit.pack(side=tk.RIGHT)

    def clear_entry(self):
        self.entry_date.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.entry_food.delete(0, tk.END)
        self.entry_calories.delete(0, tk.END)

    def submit_entry(self):  # coressponding to comment about lamda --> add params date, time, food, calories
        error_found = self.validate()
        if error_found[0]:
            messagebox.showerror("Invalid Input", error_found[1])
        else:
            jm.add_food(self.entry_date.get(), self.entry_time.get(), self.entry_food.get(),
                        self.entry_calories.get())
            self.clear_entry()
            self.entry_date.insert(0, datetime.today().strftime("%m/%d/%Y"))
            self.entry_time.insert(0, datetime.now().time().strftime("%H:%M"))

    def validate(self):
        error_found = [False, ""]
        date_valid = [True, "Date incorrect format"]
        time_valid = [True, "Time incorrect format"]
        food_valid = [True, "Food entry is empty"]
        calorie_valid = [True, "Calorie needs to be integer"]
        error_list = [date_valid, time_valid, food_valid, calorie_valid]
        try:
            datetime.strptime(self.entry_date.get(), '%m/%d/%Y')
        except ValueError:
            date_valid[0] = False
        try:
            datetime.strptime(self.entry_time.get(), '%H:%M')
        except ValueError:
            time_valid[0] = False
        if self.entry_food.get() == "":
            food_valid[0] = False
        try:
            int(self.entry_calories.get())
        except ValueError:
            calorie_valid[0] = False
        for n in error_list:
            if False in n:
                error_found[1] = error_found[1] + n[1] + "\n"
                error_found[0] = True
        return error_found

    def display_data(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = JournalWindow(self.newWindow)

    def close_windows(self):
        self.master.destroy()


# Class: Window that allows displaying and minor manipulation of Journal Entry content
class JournalWindow:
    def __init__(self, master):
        self.master = master
        self.master.title('Displaying Journal')
        self.frame = tk.Frame(self.master, width=500, height=800)
        self.frame.pack()
        self.frame.pack_propagate(0)

        journal_data = jm.read_json("food_journal")  # Example being the json file name

        self.btn_show = tk.Button(self.frame, text='Show All', width=25, command=lambda: self.show_data(journal_data))
        self.btn_show.pack(side=tk.RIGHT)

        self.btn_filter = tk.Button(self.frame, text='Filter By', width=25,
                                    command=lambda: self.filter_by_date(journal_data))
        self.btn_filter.pack(side=tk.RIGHT)

        self.btn_close = tk.Button(self.frame, text='Close', width=25, command=self.close_windows)
        self.btn_close.pack(side=tk.RIGHT)

        self.filter_frame = tk.Frame(self.master)
        self.filter_frame.pack(side=tk.LEFT)

        label_time = tk.Label(self.filter_frame, text="Date to Filter by", fg="red")
        label_time.pack(side=tk.TOP)
        self.entry_filter = tk.Entry(self.filter_frame)
        self.entry_filter.pack(side=tk.BOTTOM)

    def show_data(self, journal_data):
    # Displays entire Journal Entry content        
        self.frame3 = tk.Frame(self.master)
        self.frame3.pack()

        self.txt_box = tk.Text(self.frame3)

        for key, value in journal_data.items():
            self.txt_box.insert(tk.END, key + "\n", ("key_date", 0, tk.END))
            self.txt_box.tag_configure("key_date", foreground="red", font=" TkFixedFont")
            # Perhaps use Enumerate?
            for element in value:
                # Change Name, Time, and Calories color/font/size
                self.txt_box.insert(tk.END, "Name: " + element["name"] + "\n", ("next_line", 0, tk.END))
                self.txt_box.insert(tk.END, "Time: " + element["time"] + "\n", ("next_line", 0, tk.END))
                self.txt_box.insert(tk.END, "Calories: " + str(element["calories"]) + "\n", ("next_line", 0, tk.END))

        self.txt_box.configure(state="disable")
        self.txt_box.pack()


    def filter_by_date(self, journal_data):
        # TODO: Add mutiple date and month options

        input_filter = self.entry_filter.get()
        if not input_filter: # Checks empty string
            try: # Check if Date format
                datetime.strptime(input_filter, '%m/%d/%Y')
            except ValueError:
                messagebox.showerror("Invalid Date Input", "Invalid Date Input")
        else: 
            filtered_data = {}
            for key, value in journal_data.items():
                if input_filter in key:
                    filtered_data[key] = value
            self.show_data(filtered_data)

    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = StartPage(root)
    root.mainloop()


if __name__ == '__main__':
    main()
