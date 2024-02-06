import tkinter as tk


class SecondFrame:
    def __init__(self, root):
        self.objects_dictionary = None
        self.frame = tk.Frame(root,bg="green")
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # this adds frame to window at x=0 and y=0 and then make it acquire full height and width
        self.label = tk.Label(self.frame, text="Second frame", bg='green', fg="white", font=("Helvetica", 16))  # this creates label in frame
        self.label.pack(pady=20)  # this displays label in frame
        self.button1 = tk.Button(self.frame, text="Main", command=self.open_main_frame) # this creates button in frame
        self.button1.pack(pady=(0,10))
        self.button2 = tk.Button(self.frame, text="Third", command=self.open_third_frame)  # this creates button in frame
        self.button2.pack()

    def get_frame(self):  # when other classes call this function using object of this class they get the frame
        return self.frame

    def set_objects_dictionary(self, objects_dictionary):  # when other classes call this function using object of this class they can set objects dictionary of this class
        self.objects_dictionary = objects_dictionary

    def open_main_frame(self):
        self.objects_dictionary["main_frame_obj"].get_frame().tkraise()

    def open_third_frame(self):
        self.objects_dictionary["third_frame_obj"].get_frame().tkraise()
