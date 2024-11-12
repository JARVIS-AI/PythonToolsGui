import tkinter as tk
import calendar
from tkinter import messagebox
import datetime

# Function to display the calendar for the selected month and year
def show_calendar():
    try:
        month = int(month_var.get())  # Ensure month is an integer
        year = int(year_var.get())    # Ensure year is an integer
        
        # Get the calendar for the selected month and year
        cal = calendar.month(year, month)

        # Get today's date
        today = datetime.date.today()
        today_month = today.month
        today_day = today.day
        today_year = today.year

        # Highlight today if it's in the displayed month and year
        if today_month == month and today_year == year:
            # Find the position of the day (in the calendar)
            cal_lines = cal.split('\n')
            for i, line in enumerate(cal_lines):
                if str(today_day) in line:
                    # Highlight the day by adding square brackets around it
                    cal_lines[i] = line.replace(str(today_day), f"[{today_day}]")
                    break
            
            # Join the calendar lines back together
            cal = '\n'.join(cal_lines)

        # Clear the previous calendar
        text.delete(1.0, tk.END)

        # Insert the new calendar with padding
        text.insert(tk.END, "\n" * 2 + cal + "\n" * 2)  # Adding padding around the calendar
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid month (1-12) and year.")

# Function to show an error if the year or month is invalid
def validate_input():
    try:
        month = int(month_var.get())
        year = int(year_var.get())
        if month < 1 or month > 12:
            raise ValueError
        show_calendar()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid month (1-12) and year.")

# Function to display today's calendar
def show_today():
    today = datetime.date.today()
    month_var.set(str(today.month))
    year_var.set(str(today.year))
    show_calendar()

# Function to show the "About" information
def show_about():
    messagebox.showinfo("About", "Calendar App\nThis app displays a calendar and highlights today's date.\nWritten by : Amir Mohammad Safari\n\n\nVersion: 1.0.4")

# Create the main window
root = tk.Tk()
root.title("Calendar")

# Create a frame for the input
frame = tk.Frame(root)
frame.pack(pady=10)

# Create month and year labels and entry fields
month_label = tk.Label(frame, text="Month (1-12):")
month_label.grid(row=0, column=0, padx=5)

month_var = tk.StringVar()
month_entry = tk.Entry(frame, textvariable=month_var, width=5)
month_entry.grid(row=0, column=1, padx=5)

year_label = tk.Label(frame, text="Year:")
year_label.grid(row=0, column=2, padx=5)

year_var = tk.StringVar()
year_entry = tk.Entry(frame, textvariable=year_var, width=7)
year_entry.grid(row=0, column=3, padx=5)

# Button to display the calendar
show_button = tk.Button(frame, text="Show Calendar", command=validate_input)
show_button.grid(row=0, column=4, padx=5)

# Button to show today's calendar
today_button = tk.Button(frame, text="Today", command=show_today)
today_button.grid(row=0, column=5, padx=5)

# Text widget to display the calendar with padding
text = tk.Text(root, width=20, height=10, font=("Courier", 12), padx=10, pady=5)
text.pack(pady=10)

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)

# Add the "Help" menu to the menu bar
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the root window to use the menu bar
root.config(menu=menu_bar)

# Set default month and year
month_var.set("12")
year_var.set("2024")

# Show the initial calendar
show_calendar()

# Run the application
root.mainloop()
