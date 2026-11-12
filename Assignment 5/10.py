import tkinter as tk
import tkinter.messagebox as tmsg
root = tk.Tk()
root.geometry("500x400")
root.title("Donation Application")
scale = tk.Scale(root, from_=100, to=1000, orient=tk.HORIZONTAL, label="Select Donation Amount")
scale.pack(padx=20, pady=20)
def donate():
    amount = scale.get()
    tmsg.showinfo("Donation", f"Your donation amount is Rs. {amount}")
button = tk.Button(root, text="Click to Donate", command=donate)
button.pack(padx=20, pady=20)
root.mainloop()