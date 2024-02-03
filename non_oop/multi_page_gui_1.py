import tkinter as tk

# function to open frame 1 or page 1 below
def open_frame_1():
    frame1.tkraise() # this brings frame 1 at top layer
# function to open frame 1 or page 1 above

# function to open frame 2 or page 2 below
def open_frame_2():
    frame2.tkraise() # this brings frame 2 at top layer
# function to open frame 2 or page 2 above


root=tk.Tk() # this creates object of Tk class
root.title('Multiple Frames') # this sets title of window
root.geometry('800x500') # this sets size of window

# code to create menu below
menu_bar=tk.Menu(root) #this creates menu
menu_bar.add_command(label="Page1", command=open_frame_1) # this add menu item
menu_bar.add_command(label="Page2", command=open_frame_2) # this add menu item
root.config(menu=menu_bar) # this adds menu to window
# code to create menu above


frame1=tk.Frame(root,bg="red") # this creates frame1
frame2=tk.Frame(root,bg="green") # this creates frame2

frame1.place(x=0, y=0, relwidth=1, relheight=1) # this adds frame1 to window at x=0 and y=0 and then make it acquire full height and width
frame2.place(x=0, y=0, relwidth=1, relheight=1) # this adds frame2 to window at x=0 and y=0 and then make it acquire full height and width

label1=tk.Label(frame1,text="This is Frame 1",bg='red',fg="white",font=("Helvetica", 16)) # this creates label in frame1
label2=tk.Label(frame2,text="This is Frame 2",bg='green',fg="white",font=("Helvetica", 16)) # this creates label in frame2

label1.pack(pady=30) # this displays label1 in frame1
label2.pack(pady=30) # this displays label2 in frame2

open_frame_1() # this function is called once to display frame1 in beginning

root.mainloop() # this runs the window
