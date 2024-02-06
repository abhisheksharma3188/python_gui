import tkinter as tk
from main_frame import MainFrame
from second_frame import SecondFrame
from third_frame import ThirdFrame


class App:
    def __init__(self):
        self.root = tk.Tk()

        # code to create menu below
        self.menu_bar = tk.Menu(self.root)  # this creates menu
        self.menu_bar.add_command(label="Main", command=self.open_main_frame)  # this adds menu item
        self.menu_bar.add_command(label="Insert", command=self.open_second_frame)  # this add menu item
        self.menu_bar.add_command(label="View", command=self.open_third_frame)  # this adds menu item
        self.root.config(menu=self.menu_bar)  # this adds menu to window
        # code to create menu above

        self.objects_dictionary = {} # this sets dictionary of objects which is sent to all frame classes so that every frame class can use functions of other frame classes

        self.main_frame_obj = MainFrame(self.root)  # this creates object of MainFrame class
        self.objects_dictionary["main_frame_obj"] = self.main_frame_obj # this fills objects dictionary

        self.second_frame_obj = SecondFrame(self.root)  # this creates object of SecondFrame class
        self.objects_dictionary["second_frame_obj"] = self.second_frame_obj # this fills objects dictionary

        self.third_frame_obj = ThirdFrame(self.root)  # this creates object of ThirdFrame class
        self.objects_dictionary["third_frame_obj"] = self.third_frame_obj # this fills objects dictionary

        self.main_frame_obj.set_objects_dictionary(self.objects_dictionary) # this sets objects dictionary of MainFrame class
        self.second_frame_obj.set_objects_dictionary(self.objects_dictionary) # this sets objects dictionary of SecondFrame class
        self.third_frame_obj.set_objects_dictionary(self.objects_dictionary) # # this sets objects dictionary of ThirdFrame class

        self.open_main_frame() # this opens main_frame in beginning

        self.root.mainloop()

    def open_main_frame(self):
        self.main_frame_obj.get_frame().tkraise()

    def open_second_frame(self):
        self.second_frame_obj.get_frame().tkraise()

    def open_third_frame(self):
        self.third_frame_obj.get_frame().tkraise()


app = App()
