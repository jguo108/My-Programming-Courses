# https://projects.raspberrypi.org/en/projects/rocket-launch/0

# TODO:
# - show result of succes or failure
# - let user to relaunch by clicking the 'launch' button

import tkinter as tk

WIDTH = 400
HEIGHT = 400

burn = 100  # how much fuel
orbit_radius = 250
orbit_y = 150

fuel = 0


def launch_clicked():
    global fuel
    fuel = int(entry.get())
    launch()


def launch():
    global canvas, rocket, fuel, burn, fuel_indicator

    rocket_y = canvas.coords(rocket)[1]
    if fuel >= burn and rocket_y > orbit_y:
        fuel -= burn
        # print(f'Fuel left: {fuel}')
        canvas.itemconfig(fuel_indicator, text=f'Fuel left: {fuel}')
        canvas.move(rocket, 0, -1)
        window.after(10, launch)

    if fuel < burn and rocket_y > orbit_y:
        fall()
    else:
        pass  # Success


window = tk.Tk()
window.geometry('400x440')
window.resizable(False, False)
canvas = tk.Canvas(
    window,
    width=WIDTH,
    height=HEIGHT,
    background='black')
canvas.grid(row=0, column=0, columnspan=3)

label = tk.Label(window, text='Fuel(tons)')
label.grid(row=1, column=0, sticky='e')

entry = tk.Entry(window)
entry.grid(row=1, column=1, sticky='w')

button = tk.Button(window, text="launch", command=launch_clicked)
button.grid(row=1, column=2, sticky='w')


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

# Fuel indicator
fuel_indicator = canvas.create_text(
    10, 10, text=f'Fuel left: {fuel}', fill='gray90', font=('Orbitron', 12), anchor='nw')


def fall():
    rocket_y = canvas.coords(rocket)[1]
    if rocket_y < HEIGHT+20:
        canvas.move(rocket, 0, 1)
        window.after(100, fall)


# fuel = int(input('How many kilograms of fuel do you want to use?'))

# launch()
window.mainloop()
