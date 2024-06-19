import tkinter as tk


def update_text():
    global text_content
    # Update the text content
    text_content += "."
    # Update the text item on the canvas
    canvas.itemconfig(text_item, text=text_content)
    # Schedule the next update
    canvas.after(10, update_text)


# Create the main window
window = tk.Tk()

# Create a canvas widget
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Add text to the canvas
text_content = ""
text_item = canvas.create_text(50, 50, text=text_content, font=('Arial', 12))

# Start the update loop
update_text()

# Run the main event loop
window.mainloop()
