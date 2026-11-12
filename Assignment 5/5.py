import tkinter as tk
root = tk.Tk()
root.geometry("500x400")
def button_press():
    print("Button was clicked successfully!")
button = tk.Button(
    root,
    text="Click Here",
    command=button_press
)
button.pack(padx=20, pady=20)
root.mainloop()