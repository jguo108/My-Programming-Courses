import tkinter as tk


root = tk.Tk()
root.title("Grid Layout")
root.geometry('600x800')

# Create a grid layout
for i in range(7):
    root.rowconfigure(i, weight=1)
    for j in range(4):
        root.columnconfigure(j, weight=1)

# Create a label that spans the first two rows
label = tk.Label(root, text="",
                 font="arial 30", bg='gray25')
label.grid(row=0, column=0, columnspan=4, rowspan=2, sticky='nwse')

root.mainloop()
