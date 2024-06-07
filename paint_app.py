import tkinter as tk
from tkinter import colorchooser

window = tk.Tk()
window.title("Paint!")

canvas = tk.Canvas(window, width=600, height=600, background="white")
canvas.grid_configure(row=1, column=0, columnspan=15)
canvas.is_mouse_down = False
canvas.color = "#000000"
canvas.mode = "pen"
canvas.prev_mouse_x = 0
canvas.prev_mouse_y = 0

size_slider = tk.Scale(window, from_=2, to_=25, orient="horizontal")
size_slider.set(12)
size_slider.grid_configure(row=0, column=0)

def mouse_down(event):
    w = size_slider.get()
    if canvas.mode == "smiley":
        canvas.create_text(event.x, event.y, text=":)", angle=270, font=("Arial", 4*w), fill=canvas.color)
        canvas.is_mouse_down = True
    else:
        canvas.is_mouse_down = True
        canvas.prev_mouse_x = event.x
        canvas.prev_mouse_y = event.y
        draw_circle(event.x, event.y)


def mouse_up(event):
    canvas.is_mouse_down = False


def mouse_move(event):
    if canvas.is_mouse_down:
        width = size_slider.get()
        if canvas.mode == "smiley":
            draw_smiley(event.x, event.y)
        else:
            canvas.create_line(canvas.prev_mouse_x, canvas.prev_mouse_y, event.x, event.y, fill=get_draw_color(), width=width)
            draw_circle(event.x, event.y)

            canvas.prev_mouse_x = event.x
            canvas.prev_mouse_y = event.y


canvas.bind("<Button-1>", mouse_down)
canvas.bind("<ButtonRelease-1>", mouse_up)
canvas.bind("<Motion>", mouse_move)


def draw_circle(x, y):
    width = size_slider.get()
    canvas.create_oval(x - width/2, y - width/2, x + width/2 - 1, y + width/2 - 1, fill=get_draw_color(), width=0)


def draw_smiley(x, y):
    width = size_slider.get()
    canvas.create_text(x, y, text=":)", angle=270, font=("Arial", 4 * width), fill=get_draw_color())


def pick_color_pressed():
    canvas.color = get_color("Brush color", "#FF0000")


def pick_bg_color_pressed():
    canvas.configure(background=get_color("Background", "#FFFFFF"))


def get_color(title, default):
    picked = colorchooser.askcolor(title=title, initialcolor=default)
    if picked[1] is not None:
        return picked[1]

    return default


pick_color_button = tk.Button(window, text="Brush color", command=pick_color_pressed)
pick_color_button.grid_configure(row=0, column=1)

pick_bg_color_button = tk.Button(window, text="Background color", command=pick_bg_color_pressed)
pick_bg_color_button.grid_configure(row=0, column=5)


def scale():
    canvas.scale("all", 0, 0, 2, 2)
    canvas.configure(width=1200, height=1200)


def clear_all():
    canvas.delete("all")


erase_all_button = tk.Button(window, text="Erase all", command=clear_all)
erase_all_button.grid_configure(row=0, column=6)


def pick_eraser():
    canvas.mode="eraser"


def pick_pen():
    canvas.mode = "pen"


def pick_smiley():
    canvas.mode = "smiley"


pick_eraser_button = tk.Button(window, text="Eraser", command=pick_eraser)
pick_eraser_button.grid_configure(row=0, column=2)

pick_pen_button = tk.Button(window, text="Pen", command=pick_pen)
pick_pen_button.grid_configure(row=0, column=3)

pick_pen_button = tk.Button(window, text=":)", command=pick_smiley)
pick_pen_button.grid_configure(row=0, column=4)


def get_draw_color() -> str:
    if canvas.mode == "eraser":
        return "#FFFFFF"

    return canvas.color


window.mainloop()
