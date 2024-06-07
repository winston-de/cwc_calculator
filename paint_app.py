import tkinter
import tkinter as tk
from PIL import Image
import io
from tkinter.filedialog import asksaveasfile
from tkinter import colorchooser


window = tk.Tk()
window.title("Paint")

canvas = tk.Canvas(window, width=600, height=600, background="white")

canvas.is_mouse_down = False
canvas.prev_x = 0
canvas.prev_y = 0


def mouse_down(event: tkinter.Event):
    canvas.is_mouse_down = True
    canvas.prev_x = event.x
    canvas.prev_y = event.y
    draw_circle(canvas.prev_x, canvas.prev_y)


def mouse_up(event):
    canvas.is_mouse_down = False


def mouse_motion(event):
    if canvas.is_mouse_down:
        w = width_slider.get()
        color = canvas.color
        draw_circle(canvas.prev_x, canvas.prev_y)
        canvas.create_line(canvas.prev_x, canvas.prev_y, event.x, event.y, fill=color, width=w)
        draw_circle(event.x, event.y)
        canvas.prev_x = event.x
        canvas.prev_y = event.y

def draw_circle(x, y):
    w = width_slider.get()
    color = canvas.color
    canvas.create_oval(x - w / 2, y - w / 2, x + w / 2 - 1, y + w / 2 - 1, fill=color, width=0)


canvas.bind("<Button-1>", mouse_down)
canvas.bind('<ButtonRelease-1>', mouse_up)
canvas.bind('<Motion>', mouse_motion)


def save_canvas():
    canvas.update()
    f = asksaveasfile(initialfile='Image.jpg',
                      defaultextension=".jpg", filetypes=[("All Files", "*.*"), ("Image", "*.jpg")])

    ps = canvas.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save(f)


save_button = tk.Button(text="Save", command=save_canvas)


def get_color(title, default) -> str:
    picked = colorchooser.askcolor(title=title, initialcolor=default)
    if picked[1] is not None:
        return picked[1]

    return default


def pick_color():
    canvas.color = get_color("Pick brush color", "#FF0000")
    pen_button.color = canvas.color


def pick_color_bg():
    bg = get_color("Pick background color", "#FFFFFF")
    canvas.configure(background=bg)


canvas.color = "#000000"
pick_color_button = tk.Button(text="Brush color", command=pick_color)
pick_background_button = tk.Button(text="BG color", command=pick_color_bg)


def pick_pen():
    canvas.color = pen_button.color
    pen_button["state"] = "disabled"
    eraser_button["state"] = "normal"


def pick_eraser():
    canvas.color = "#FFFFFF"
    pen_button["state"] = "normal"
    eraser_button["state"] = "disabled"


def clear_all():
    canvas.delete("all")

pen_button = tk.Button(text="Pen", command=pick_pen)
pen_button.color = "#000000"

eraser_button = tk.Button(text="Eraser", command=pick_eraser)
erase_all_button = tk.Button(text="Erase all", command=clear_all)
pick_pen()

width_slider = tk.Scale(window, from_=2, to_=25, orient="horizontal")


pick_background_button.grid_configure(row=0, column=0)
pick_color_button.grid_configure(row=0, column=1)
pen_button.grid_configure(row=0, column=2)
width_slider.grid_configure(row=0, column=3)
eraser_button.grid_configure(row=0, column=4)
erase_all_button.grid_configure(row=0, column=5)
save_button.grid_configure(row=0, column=6)
canvas.grid_configure(row=1, columnspan=10)

window.mainloop()