# Creates the application window
import JSONmaker as jm
import tkinter as tk
# food_journal is an array containing the food journal entries
# food_dictionary is a dictionary of foods and their calories
food_journal = {}
food_cal = {}
#TODO: Address the global versus local copies (between main and JSONmaker.py)


#Code review on param --> Self and master usage
class StartPage:
    def __init__(self, master):
        self.master = master
        self.master.title('Food Journal Home Page')
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(ipadx=50, ipady=50)       

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

        self.button_frames = tk.Frame()
        self.button_frames.pack()

        #Button that when pressed creates and opens a new class/window 
        self.btn_display = tk.Button(self.button_frames, text = 'Display Journal', width = 20, bg = 'lightblue', command = self.display_data)
        self.btn_display.pack()

        self.btn_submit = tk.Button(self.button_frames, text="Submit", width = 10, command = self.submit_entry) #in case its needed (command=lambda : self.submit_entry(entry_date.get(), entry_time.get(), entry_food.get(), entry_calories.get())
        self.btn_submit.pack(side=tk.RIGHT)

        self.btn_clear = tk.Button(self.button_frames, text="Clear", width = 10, command = self.clear_entry)
        self.btn_clear.pack(side=tk.RIGHT)

        self.btn_quit = tk.Button(self.button_frames, text="Quit", width = 10, command = self.close_windows)
        self.btn_quit.pack(side=tk.RIGHT)


    def clear_entry(self):
        self.entry_date.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.entry_food.delete(0, tk.END)
        self.entry_calories.delete(0, tk.END)

    # Non Operational right now
    def submit_entry(self): #coressponding to comment about lamda --> add params date, time, food, calories
        jm.initialize_data()
        temp = jm.add_food(self.entry_date.get(), self.entry_time.get(), self.entry_food.get(), self.entry_calories.get())
        print(temp)
        jm.write_json('food_journal', food_journal)
        self.clear_entry()

    def display_data(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = JournalWindow(self.newWindow)

    def close_windows(self):
        self.master.destroy()

class JournalWindow:
    def __init__(self, master):
        self.master = master
        self.master.title('Displaying Journal')
        self.frame = tk.Frame(self.master)

        self.btn_show = tk.Button(self.frame, text = 'Show', width = 25, command = self.show_data)
        self.btn_show.pack()
        
        self.btn_quit = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.btn_quit.pack()
        
        self.frame.pack()

    def show_data(self):
        data = jm.read_json("Example") #Example being the json file name
        self.txt_box = tk.Text(self.master)
        self.txt_box.pack()

        for key, value in data.items():
            self.txt_box.insert(tk.END, key + "\n", ("key_date", 0, tk.END))
            self.txt_box.tag_configure("key_date", foreground = "red", font = " TkFixedFont")
            # Perhaps use Enumerate?
            for element in value:
                #Change Name, Time, and Calories color/font/size
                self.txt_box.insert(tk.END, "Name: " + element["name"] + "\n", ("next_line", 0, tk.END))
                self.txt_box.insert(tk.END, "Time: " + element["time"] + "\n", ("next_line", 0, tk.END))
                self.txt_box.insert(tk.END, "Calories: " + str(element["calories"]) + "\n", ("next_line", 0, tk.END))
    
    def close_windows(self):
        self.master.destroy()
    
        
def main():
    root = tk.Tk()
    app = StartPage(root)
    root.mainloop()

if __name__ == '__main__':
    main()