import tkinter as tk
from frame1 import Frame1
from frame2 import Frame2
class Multipage_App(): # create Multipage_App class
    def __init__(self): # __init__ function is called as soon as we made object of class
        self.root = tk.Tk()  # this creates object of Tk class
        self.root.title('Multiple Frames')  # this sets title of window
        self.root.geometry('800x500')  # this sets size of window

        # code to create menu below
        menu_bar = tk.Menu(self.root)  # this creates menu
        menu_bar.add_command(label="Page1", command=self.open_frame_1)  # this add menu item
        menu_bar.add_command(label="Page2", command=self.open_frame_2)  # this add menu item
        self.root.config(menu=menu_bar)  # this adds menu to window
        # code to create menu above

        frame_1 = Frame1(self.root) # this creates object of Frame1 class
        frame_2 = Frame2(self.root) # this creates object of Frame2 class

        self.f1 = frame_1.get_frame() # this gets frame from frame1 class
        self.f2 = frame_2.get_frame() # this gets frame from frame2 class

        self.open_frame_1()  # this function is called once to display frame1 in beginning

        self.root.mainloop()  # this runs the window

    def open_frame_1(self):
        self.f1.tkraise()
    def open_frame_2(self):
        self.f2.tkraise()

multipage_app = Multipage_App() # this creates object of Multipage_App class and starts the app
