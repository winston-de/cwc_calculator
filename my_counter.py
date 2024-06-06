import tkinter
import tkinter as tk

window = tk.Tk()
window.title("Hello!")

label = tk.Label(window, text="Start counting!!")
label.pack()
label.count = 0

def update_counter():
    label.count += 1
    label.config(text=f"Count: {label.count}")


button = tk.Button(window, text="Click me!", command=update_counter)
button.pack()

window.mainloop()