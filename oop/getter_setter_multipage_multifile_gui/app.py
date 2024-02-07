import tkinter as tk
from first_frame import FirstFrame
from second_frame import SecondFrame


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.state("zoomed")

        # code to create menu below
        self.menu_bar = tk.Menu(self.root)  # this creates menu
        self.menu_bar.add_command(label="First Frame", command=self.open_first_frame)  # this adds menu item
        self.menu_bar.add_command(label="Second Frame", command=self.open_second_frame)  # this add menu item
        self.root.config(menu=self.menu_bar)  # this adds menu to window
        # code to create menu above

        self.objects_dictionary = {} # this sets dictionary of objects which is sent to all frame classes so that every frame class can use functions of other frame classes

        self.first_frame_obj = FirstFrame(self.root)  # this creates object of MainFrame class
        self.objects_dictionary["first_frame_obj"] = self.first_frame_obj # this fills objects dictionary

        self.second_frame_obj = SecondFrame(self.root)  # this creates object of SecondFrame class
        self.objects_dictionary["second_frame_obj"] = self.second_frame_obj  # this fills objects dictionary

        self.first_frame_obj.set_objects_dictionary(self.objects_dictionary)  # this sets objects dictionary of MainFrame class
        self.second_frame_obj.set_objects_dictionary(self.objects_dictionary)  # this sets objects dictionary of SecondFrame class

        self.open_first_frame()  # this opens main_frame in beginning

        self.root.mainloop()

    def open_first_frame(self):  # this opens first frame
        self.first_frame_obj.get_frame().tkraise()

    def open_second_frame(self):  # this opens second frame
        self.second_frame_obj.get_frame().tkraise()


app = App()
