import tkinter as tk

window = tk.Tk()
window.title("Calculator")

title_label = tk.Label(window, text="Calculator")
title_label.grid_configure(row=0, column=0, columnspan=4)

number_label = tk.Label(window, text="0")
number_label.grid_configure(row=1, column=0, columnspan=4)
number_label.num_string = "0"

result_label = tk.Label(window, text="")
result_label.string = ""
result_label.grid_configure(row=2, column=0, columnspan=4)
result_label.reset_needed = False

button_start_row = 3


def add_number(value):
    if number_label.num_string == "0":
        number_label.num_string = ""

    if result_label.reset_needed:  # clear result display for new calculation
        result_label.string = ""
        result_label.configure(text="")
        result_label.reset_needed = False

    number_label.num_string += str(value)
    number_label.configure(text=number_label.num_string)


def create_number_buttons():
    def create_number_button_helper(val, row, col):
        button = tk.Button(text=str(val), command=lambda: add_number(val))
        button.grid_configure(row=button_start_row + row, column=col)

    cur_row = 0
    cur_col = 0

    for i in range(1, 10):
        create_number_button_helper(i, cur_row, cur_col)

        cur_col += 1

        if cur_col >= 3:
            cur_col = 0
            cur_row += 1

    create_number_button_helper(0, 3, 1)


create_number_buttons()

nums = []
operators = []


def add_operator(op):
    operators.append(op)
    num = float(number_label.num_string)
    nums.append(num)
    clear_number()
    result_label.string += f"{num} {op} "
    result_label.configure(text=result_label.string)


def clear_number():
    number_label.num_string = "0"
    number_label.configure(text=number_label.num_string)


def do_operations():
    if len(nums) == 0:
        return

    last_num = float(number_label.num_string)
    nums.append(last_num)

    num = nums[0]
    for i in range(0, len(operators)):
        op = operators[i]
        cur_num = nums[i + 1]
        if op == "+":
            num += cur_num
        elif op == "-":
            num -= cur_num
        elif op == "*":
            num *= cur_num
        elif op == "/":
            num /= cur_num
        elif op == "^":
            num = num**cur_num

    result_label.string += f"{last_num} = {num}"
    result_label.configure(text=result_label.string)
    result_label.reset_needed = True
    clear_all()


def clear_all():
    clear_number()
    nums.clear()
    operators.clear()


def negate():
    if number_label.num_string.find("-") == -1:  # add the -
        number_label.num_string = "-" + number_label.num_string
    else:  # remove the -
        number_label.num_string = number_label.num_string.replace("-", "")

    number_label.configure(text=number_label.num_string)


def delete():
    if len(number_label.num_string) <= 1:
        number_label.num_string = "0"
    else:
        number_label.num_string = number_label.num_string[:-1]

    number_label.configure(text=number_label.num_string)


def add_decimal():
    index = number_label.num_string.find(".")
    if index == -1:
        add_number(".")
    elif index == len(number_label.num_string) - 1:  # toggle decimal
        number_label.num_string = number_label.num_string.replace(".", "")
        number_label.configure(text=number_label.num_string)


def create_operator_buttons():
    button_plus = tk.Button(text="+", command=lambda : add_operator("+"))
    button_plus.grid_configure(row=button_start_row, column=3)
    button_plus = tk.Button(text="–", command=lambda : add_operator("-"))
    button_plus.grid_configure(row=button_start_row+1, column=3)
    button_plus = tk.Button(text="*", command=lambda : add_operator("*"))
    button_plus.grid_configure(row=button_start_row + 2, column=3)
    button_plus = tk.Button(text="/", command=lambda : add_operator("/"))
    button_plus.grid_configure(row=button_start_row + 3, column=3)
    button_plus = tk.Button(text="^", command=lambda : add_operator("^"))
    button_plus.grid_configure(row=button_start_row + 4, column=0)

    button_plus = tk.Button(text="⌫", command=delete)
    button_plus.grid_configure(row=button_start_row + 4, column=1)
    button_plus = tk.Button(text=".", command=add_decimal)
    button_plus.grid_configure(row=button_start_row + 4, column=2)
    button_plus = tk.Button(text="C", command=clear_all)
    button_plus.grid_configure(row=button_start_row + 4, column=3)
    button_plus = tk.Button(text="-", command=negate)
    button_plus.grid_configure(row=button_start_row + 3, column=0)
    button_equals = tk.Button(text="=", command=do_operations)
    button_equals.grid_configure(row=button_start_row + 3, column=2)


create_operator_buttons()

window.mainloop()
