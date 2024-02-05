import tkinter as tk

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Scrollable Form Example")

root.state('zoomed')
root.geometry("800x500")

canvas = tk.Canvas(root)
scrollbar_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar_x = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
frame = tk.Frame(canvas)

canvas.create_window((0, 0), window=frame, anchor="nw", width=canvas.winfo_screenwidth())
canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

scrollbar_y.pack(side="right", fill="y")
scrollbar_x.pack(side="bottom", fill="x")
canvas.pack(side="left", fill="both", expand=True)

root.bind("<Configure>", on_canvas_configure)

# Add widgets to the form_frame (the scrollable area)
for i in range(101):
    label = tk.Label(frame, text=f"Label {i} ")
    label.pack(padx=20, pady=20)

root.mainloop()
