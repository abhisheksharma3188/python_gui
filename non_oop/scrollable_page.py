import tkinter as tk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Create main window
root = tk.Tk()
root.title("Scrollable Grid Example")

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical")

# Create a Canvas widget
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)

# Create a frame inside the canvas
frame = tk.Frame(canvas)

# Add labels to the frame
for x in range(1, 101):
    tk.Label(frame, text=f"My Label {x}").pack()

# Create window inside the canvas
canvas.create_window((0, 0), window=frame, anchor="nw")

# Configure the scrollbar to scroll the canvas
scrollbar.config(command=canvas.yview)

# Bind the event to update the scroll region
frame.bind("<Configure>", on_configure)

# Pack the scrollbar to the right
scrollbar.pack(side="right", fill="y")

# Run the main loop
root.mainloop()
