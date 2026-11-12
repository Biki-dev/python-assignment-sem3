import tkinter as tk
import tkinter.messagebox as tmsg
root = tk.Tk()
root.geometry("500x400")
root.title("Message Box Application")
def show_message():
    tmsg.showinfo("Greetings", "Welcome to Tkinter GUI!")
button = tk.Button(root, text="Show Message", command=show_message)
button.pack(padx=20, pady=20)
root.mainloop()