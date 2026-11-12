import tkinter as tk
root = tk.Tk()
root.geometry("500x400")
label = tk.Label(
    root,
    text="Welcome to python Lab!",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="navy"
)
label.pack(padx=20, pady=20)
root.mainloop()