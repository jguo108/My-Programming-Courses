# https://projects.raspberrypi.org/en/projects/rocket-launch/0

# TODO:

import tkinter as tk

WIDTH = 400
HEIGHT = 400

burn = 100  # how much fuel
orbit_radius = 250
orbit_y = 150

window = tk.Tk()
window.resizable(False, False)
canvas = tk.Canvas(
    window,
    width=WIDTH,
    height=HEIGHT,
    background='black')
canvas.pack()

earth_image = tk.PhotoImage(file='Resources/rocket_launch/earth.png')
earth_resized_image = earth_image.subsample(16, 16)
canvas.create_image(
    WIDTH/2, HEIGHT, image=earth_resized_image, anchor="center")

rocket_image = tk.PhotoImage(file='Resources/rocket_launch/rocket.png')
rocket_resized_image = rocket_image.subsample(128, 128)
rocket = canvas.create_image(
    WIDTH/2, 350, image=rocket_resized_image, anchor="center")

# Orbit
canvas.create_arc(WIDTH/2-orbit_radius, HEIGHT-orbit_radius,
                  WIDTH/2+orbit_radius, HEIGHT + orbit_radius, start=0, extent=180,
                  style=tk.ARC, outline='white', width=3)


def fall():
    rocket_y = canvas.coords(rocket)[1]
    if rocket_y < HEIGHT+20:
        canvas.move(rocket, 0, 1)
        window.after(100, fall)


def launch():
    global canvas, rocket, fuel, burn
    rocket_y = canvas.coords(rocket)[1]
    if fuel >= burn and rocket_y > orbit_y:
        fuel -= burn
        print(f'Fuel left: {fuel}')
        canvas.move(rocket, 0, -1)
        window.after(10, launch)

    if fuel < burn and rocket_y > orbit_y:
        fall()
    else:
        pass  # Success


fuel = int(input('How many kilograms of fuel do you want to use?'))

launch()
window.mainloop()
