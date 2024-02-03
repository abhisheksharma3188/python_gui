import tkinter as tk
from tkinter import ttk

def enter_data():
    print(f'First Name : {first_name_entry.get()}')
    print(f'Last Name : {last_name_entry.get()}')
    print(f'Title : {title_combobox.get()}')
    print(f'Age : {age_spinbox.get()}')
    print(f'Nationality : {nationality_combobox.get()}')
    print(f'Registered : {registered_var.get()}')
    print(f'# Courses : {numcourses_spinbox.get()}')
    print(f'# Semesters : {numsemesters_spinbox.get()}')
    print(f'Terms & Condition : {terms_var.get()}')




root = tk.Tk()
root.title("Data Entry Form")

frame = tk.Frame(root)
frame.pack()

user_info_frame = tk.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tk.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = tk.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_entry = tk.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title = tk.Label(user_info_frame, text='Title')
title.grid(row=0, column=2)

title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms", "Dr."])
title_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0)

age_spinbox=tk.Spinbox(user_info_frame, from_=18, to=110)
age_spinbox.grid(row=3, column=0)

nationality_label = tk.Label(user_info_frame, text="Nationality")
nationality_label.grid(row=2, column=1)

nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "South America", "Oceania"])
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

course_frame = tk.LabelFrame(frame)
course_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

registered_var=tk.IntVar()
registered_label = tk.Label(course_frame, text="Registration Status")
registered_label.grid(row=0, column=0)

registered_check = tk.Checkbutton(course_frame, text="Currently Registered", variable=registered_var)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(course_frame, text="# Completed Courses")
numcourses_label.grid(row=0, column=1)

numcourses_spinbox = tk.Spinbox(course_frame, from_=0, to="infinity")
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tk.Label(course_frame, text="# Semesters")
numsemesters_label.grid(row=0, column=2)

numsemesters_spinbox = tk.Spinbox(course_frame, from_=0, to="infinity")
numsemesters_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tk.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

terms_var=tk.IntVar()
terms_check = tk.Checkbutton(terms_frame, text="I accept terms and conditions.", variable=terms_var)
terms_check.grid(row=0, column=0, padx=10, pady=5)

button=tk.Button(frame, text="Enter Data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

root.mainloop()
