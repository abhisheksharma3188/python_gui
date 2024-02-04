import tkinter as tk


class ThirdFrame:
    def __init__(self, root):
        self.frames_dictionary = None
        self.frame = tk.Frame(root,bg="blue")
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # this adds frame to window at x=0 and y=0 and then make it acquire full height and width
        self.label = tk.Label(self.frame, text="Third frame", bg='blue', fg="white", font=("Helvetica", 16))  # this creates label in frame
        self.label.pack(pady=30)  # this displays label in frame
        self.button = tk.Button(self.frame, text="Main", command=self.open_main_frame) # this creates button in frame
        self.button.pack()

    def get_frame(self):
        return self.frame

    def set_frames_dictionary(self, frames_dictionary):
        self.frames_dictionary = frames_dictionary

    def open_main_frame(self):
        self.frames_dictionary["main_frame"].tkraise()
