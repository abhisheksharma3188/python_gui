import tkinter as tk
from main_frame import MainFrame
from second_frame import SecondFrame
from third_frame import ThirdFrame


class App:
    def __init__(self):
        self.root = tk.Tk()

        # code to create menu below
        self.menu_bar = tk.Menu(self.root)  # this creates menu
        self.menu_bar.add_command(label="Main", command=lambda: self.open_frame(self.main_frame))  # this adds menu item
        self.menu_bar.add_command(label="Insert", command=lambda: self.open_frame(self.second_frame))  # this add menu item
        self.menu_bar.add_command(label="View", command=lambda:self.open_frame(self.third_frame))  # this adds menu item
        self.root.config(menu=self.menu_bar)  # this adds menu to window
        # code to create menu above

        self.frames_dictionary={}

        self.main_frame_obj = MainFrame(self.root)  # this creates object of Frame1 class
        self.main_frame = self.main_frame_obj.get_frame()
        self.frames_dictionary["main_frame"]=self.main_frame

        self.second_frame_obj = SecondFrame(self.root)  # this creates object of Frame1 class
        self.second_frame = self.second_frame_obj.get_frame()
        self.frames_dictionary["insert_frame"] = self.second_frame

        self.third_frame_obj = ThirdFrame(self.root)  # this creates object of Frame1 class
        self.third_frame = self.third_frame_obj.get_frame()
        self.frames_dictionary["view_frame"] = self.third_frame

        self.main_frame_obj.set_frames_dictionary(self.frames_dictionary)
        self.second_frame_obj.set_frames_dictionary(self.frames_dictionary)
        self.third_frame_obj.set_frames_dictionary(self.frames_dictionary)

        self.open_frame(self.main_frame)

        self.root.mainloop()

    @staticmethod
    def open_frame(frame):
        frame.tkraise()

    def get_main_frame(self):
        return self.main_frame


app = App()
