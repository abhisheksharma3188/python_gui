import tkinter as tk

class Multipage_App: # create Multipage_App class
    def __init__(self): # __init__ function is called as soon as we made object of class
        root.title('Multiple Frames')  # this sets title of window
        root.geometry('800x500')  # this sets size of window

        # code to create menu below
        menu_bar = tk.Menu(root)  # this creates menu
        menu_bar.add_command(label="Page1", command=self.open_frame_1)  # this add menu item
        menu_bar.add_command(label="Page2", command=self.open_frame_2)  # this add menu item
        root.config(menu=menu_bar)  # this adds menu to window
        # code to create menu above

        frame_1 = Frame1() # this creates object of Frame1 class
        frame_2 = Frame2() # this creates object of Frame2 class

        self.f1 = frame_1.get_frame() # this gets frame from frame1 class
        self.f2 = frame_2.get_frame() # this gets frame from frame2 class

        self.open_frame_1()  # this function is called once to display frame1 in beginning

        root.mainloop()  # this runs the window

    def open_frame_1(self):
        self.f1.tkraise()
    def open_frame_2(self):
        self.f2.tkraise()


class Frame1:
    def __init__(self): # __init__ function is called as soon as we made object of class
        self.frame = tk.Frame(root, bg="red")  # this creates frame
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # this adds frame to window at x=0 and y=0 and then make it acquire full height and width
        self.label = tk.Label(self.frame, text="This is Frame 1", bg='red', fg="white", font=("Helvetica", 16))  # this creates label in frame
        self.label.pack(pady=30)  # this displays label in frame

    def get_frame(self): # this function returns frame
        return self.frame


class Frame2:
    def __init__(self):
        self.frame=tk.Frame(root, bg="green")  # this creates frame
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # this adds frame to window at x=0 and y=0 and then make it acquire full height and width
        self.label = tk.Label(self.frame, text="This is Frame 2", bg='green', fg="white", font=("Helvetica", 16))  # this creates label in frame
        self.label.pack(pady=30)  # this displays label in frame

    def get_frame(self): # this function returns frame
        return self.frame

root = tk.Tk()  # this creates object of Tk class
multipage_app = Multipage_App() # this creates object of Multipage_App class and starts the app
