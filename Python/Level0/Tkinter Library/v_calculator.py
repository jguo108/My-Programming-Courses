import tkinter as tk

GRID_ROWS = 7
GRID_COLS = 4
BUTTON_PADX = 5
BUTTON_PADY = 5

BUTTON_FONT = 'arial 18 bold'
BUTTON_BORDER = 1
BUTTON_FG_COLOR = 'gray80'
BUTTON_BG_COLOR = 'gray15'

equation = ''

window = tk.Tk()
window.title("Simple Calculator")
window.geometry('400x400')
window.resizable(False, False)
window.configure(bg="#17161b")


def show(symbol):
    global equation, label_result
    equation += symbol
    label_result.config(text=equation)


def clear():
    global equation, label_result
    equation = ''
    label_result.config(text=equation)


def calculate():
    global equation, label_result
    result = ''
    if equation != '':
        try:
            result = eval(equation)
        except:
            result = 'Error'
    label_result.config(text=str(result))
    equation = ''


# TODO: understand what this really means
for r in range(GRID_ROWS):
    window.rowconfigure(r, weight=1)
for c in range(GRID_COLS):
    window.columnconfigure(c, weight=1)

label_result = tk.Label(
    window, height=2, text="", font="arial 30", bg='gray20', fg='gray80', anchor='se')

# label_result = tk.Label(
#    window, text="", font="arial 30", bg='gray20', fg='gray80', anchor='se')
label_result.grid(column=0, row=0, columnspan=4, rowspan=2, sticky='nwse')

# Row 1
button_clear = tk.Button(
    window, text="C", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg='DodgerBlue2', command=lambda: clear())
button_divide = tk.Button(
    window, text="/", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('/'))
button_mod = tk.Button(
    window, text="%", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('%'))
button_multiply = tk.Button(
    window, text="*", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('*'))

button_clear.grid(
    row=2, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_divide.grid(
    row=2, column=1, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_mod.grid(
    row=2, column=2, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_multiply.grid(
    row=2, column=3, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')

# Row 3
button_7 = tk.Button(
    window, text="7", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('7'))
button_8 = tk.Button(
    window, text="8", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('8'))
button_9 = tk.Button(
    window, text="9", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('9'))
button_subtract = tk.Button(
    window, text="-", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('-'))

button_7.grid(
    row=3, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_8.grid(
    row=3, column=1, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_9.grid(
    row=3, column=2, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_subtract.grid(
    row=3, column=3, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')

# Row 4
button_4 = tk.Button(
    window, text="4", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('4'))
button_5 = tk.Button(
    window, text="5", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('5'))
button_6 = tk.Button(
    window, text="6", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('6'))
button_add = tk.Button(
    window, text="+", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('+'))

button_4.grid(
    row=4, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_5.grid(
    row=4, column=1, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_6.grid(
    row=4, column=2, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_add.grid(
    row=4, column=3, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')

# Row 5
button_1 = tk.Button(
    window, text="1", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('1'))
button_2 = tk.Button(
    window, text="2", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('2'))
button_3 = tk.Button(
    window, text="3", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('3'))
button_equal = tk.Button(
    window, text="=", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg='orange', command=calculate)

button_1.grid(
    row=5, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_2.grid(
    row=5, column=1, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_3.grid(
    row=5, column=2, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_equal.grid(
    row=5, column=3, rowspan=2, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')

# Row 6
button_0 = tk.Button(
    window, text="0", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('0'))
button_point = tk.Button(
    window, text=".", font=BUTTON_FONT, bd=BUTTON_BORDER, fg=BUTTON_FG_COLOR, bg=BUTTON_BG_COLOR, command=lambda: show('.'))

button_0.grid(
    row=6, column=0, columnspan=2, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')
button_point.grid(
    row=6, column=2, padx=BUTTON_PADX, pady=BUTTON_PADY, sticky='nwse')


window.mainloop()
