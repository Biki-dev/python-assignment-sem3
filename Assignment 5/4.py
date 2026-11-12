import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
frame = tk.Frame(
    root,
    bg="yellow",
    bd=5,
    relief=tk.SUNKEN
)
frame.pack(side=tk.LEFT, fill=tk.Y)
label = tk.Label(
    frame,
    text="Welcome to Python Lab!"
)
label.pack()
root.mainloop()