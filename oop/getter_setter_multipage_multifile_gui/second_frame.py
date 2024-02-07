import tkinter as tk


class SecondFrame:
    def __init__(self, root):
        self.objects_dictionary = None
        self.x = None

        self.frame = tk.Frame(root, bg="green")
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)  # this adds frame to window at x=0 and y=0 and then make it acquire full height and width

        self.label1 = tk.Label(self.frame, text="Second Frame", bg='green', fg="white", font=("Helvetica", 16))  # this creates label in frame
        self.label1.pack(pady=5)  # this displays label in frame

        self.button1 = tk.Button(self.frame, text="First Frame", command=self.open_first_frame) # this creates button in frame
        self.button1.pack(pady=5)

        self.entry1 = tk.Entry(self.frame, font=("Helvetica", 16))
        self.entry1.pack(pady=5)

        self.button2 = tk.Button(self.frame, text="Set X For First Frame", command=self.set_x_for_first_frame)  # this creates button in frame
        self.button2.pack(pady=5)

        self.label2 = tk.Label(self.frame, text="Value of X From First Frame : ", bg='green', fg="white", font=("Helvetica", 16))  # this creates label in frame
        self.label2.pack(pady=5)  # this displays label in frame

        self.button3 = tk.Button(self.frame, text="Get X From First Frame", command=self.get_x_from_first_frame)  # this creates button in frame
        self.button3.pack(pady=5)

    def set_objects_dictionary(self, objects_dictionary):  # when other classes call this function using object of this class they can set objects dictionary of object of this class
        self.objects_dictionary = objects_dictionary

    def get_frame(self):  # when other classes call this function using object of this class they get the frame of object of this class
        return self.frame

    def get_x(self): # when other classes call this function using object of this class they get value of x of object of this class
        return self.x

    def set_x(self, x):  # when other classes call this function using object of this class they set value of x of object of this class
        self.x = x

    def open_first_frame(self):  # this opens first frame
        self.objects_dictionary["first_frame_obj"].get_frame().tkraise()

    def set_x_for_first_frame(self):  # this sets x of object of FirstFrame
        self.objects_dictionary["first_frame_obj"].set_x(self.entry1.get())

    def get_x_from_first_frame(self):  # this gets x of object of FirstFrame
        x = self.objects_dictionary["first_frame_obj"].get_x()
        self.label2.config(text=f"Value of x From First Frame : {x}")
