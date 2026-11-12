import tkinter as tk
root = tk.Tk()
root.geometry("500x400")
root.title("Mouse Event Binding")
def button_click(event):
    print("You clicked on first button")
button = tk.Button(root, text="Click Here")
button.bind("<Button-1>", button_click)
button.pack(padx=20, pady=20)
root.mainloop()