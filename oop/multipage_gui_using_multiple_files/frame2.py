import tkinter as tk
class Frame2():
    def __init__(self,root):
        self.frame=tk.Frame(root, bg="green")  # this creates frame
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # this adds frame to window at x=0 and y=0 and then make it acquire full height and width
        self.label = tk.Label(self.frame, text="This is Frame 2", bg='green', fg="white", font=("Helvetica", 16))  # this creates label in frame
        self.label.pack(pady=30)  # this displays label in frame

    def get_frame(self): # this function returns frame
        return self.frame
