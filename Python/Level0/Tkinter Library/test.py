import tkinter as tk
import math

# Set the window size
WIDTH = 400
HEIGHT = 400

# Create the main window
window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")

# Create a canvas widget
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

angle = 0

# Create a sun object on the canvas
sun_x = WIDTH / 2
sun_y = HEIGHT / 2
sun_radius = 50
sun = canvas.create_oval(sun_x - sun_radius, sun_y - sun_radius,
                         sun_x + sun_radius, sun_y + sun_radius, fill="yellow")

# Create a planet object on the canvas
planet_radius = 20
planet_distance = 100
planet_x = sun_x + planet_distance * math.cos(angle)
planet_y = sun_y + planet_distance * math.sin(angle)
planet = canvas.create_oval(planet_x - planet_radius, planet_y - planet_radius,
                            planet_x + planet_radius, planet_y + planet_radius, fill="red")

# Update the position of the planet based on its orbit


def update_planet():
    global planet_x, planet_y, angle
    angle += 1
    planet_x = sun_x + planet_distance * math.cos(angle)
    planet_y = sun_y + planet_distance * math.sin(angle)
    canvas.coords(planet, planet_x - planet_radius, planet_y -
                  planet_radius, planet_x + planet_radius, planet_y + planet_radius)
    print((planet_x, planet_y))
    window.after(1000, update_planet)


# Start the planet orbiting
update_planet()

# Run the main event loop
window.mainloop()
