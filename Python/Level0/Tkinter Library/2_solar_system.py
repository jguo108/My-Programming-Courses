# https://projects.raspberrypi.org/en/projects/solar-system-simulator/0
# https://www.freepik.com/free-vector/classic-solar-system-scheme-with-flat-deisgn_2899001.htm#fromView=search&page=1&position=0&uuid=d19eabad-53fe-4dc5-9762-7d874bd0a5f3
# https://www.freepik.com/free-vector/colorful-solar-system-scheme-with-flat-design_2880091.htm#fromView=search&page=1&position=2&uuid=d19eabad-53fe-4dc5-9762-7d874bd0a5f3
# https://www.freepik.com/free-vector/classic-solar-system-scheme-with-flat-design_2917720.htm#fromView=search&page=1&position=10&uuid=d19eabad-53fe-4dc5-9762-7d874bd0a5f3
# https://www.freepik.com/free-vector/classic-solar-system-scheme-with-flat-design_2985040.htm#fromView=search&page=1&position=18&uuid=d19eabad-53fe-4dc5-9762-7d874bd0a5f3
import tkinter as tk
import math

# TODO:
# - use pretty images for sun and planets
# - read planet infos from csv file

WIDTH = 400
HEIGHT = 500
planets = []
sun_x = WIDTH/2
sun_y = 200
text = None
shape2planet = {}


def draw_sun():
    canvas.create_oval(
        sun_x - 50, sun_y - 50, sun_x + 50, sun_y + 50, fill="gold", width=0)


def load_planets():
    planet = {
        'name': 'Mercury',
        'color': 'saddle brown',
        'size': 16,
        'orbit': 150,
        'speed': 0.01,
        'info': 'The smallest and fastest planet'
    }
    planets.append(planet)

    planet = {
        'name': 'Venus',
        'color': 'sandy brown',
        'size': 30,
        'orbit': 200,
        'speed': 0.0075,
        'info': 'The hottest planet in the Solar System. Water would turn to steam and some metals would melt just by being there!'
    }
    planets.append(planet)

    planet = {
        'name': 'Earth',
        'color': 'deep sky blue',
        'size': 35,
        'orbit': 300,
        'speed': 0.005,
        'info': 'You are here - the only planet we know of that can support life!'
    }
    planets.append(planet)


def draw_orbits():
    for planet in planets:
        orbit_size = planet['orbit']
        canvas.create_oval(
            sun_x - orbit_size/2,
            sun_y - orbit_size/2,
            sun_x + orbit_size/2,
            sun_y + orbit_size/2,
            outline="gray")


def show_info(event):
    # 'event' has an attribute 'widget' which is the canvas
    # 'find_withtag' can be used to get items with the tag under the cursor
    # 'current' is the tag for the item under the cursor
    id = event.widget.find_withtag('current')[0]
    canvas.itemconfigure(text, text=shape2planet[id]['info'])


def hide_info(event):
    id = event.widget.find_withtag('current')[0]
    canvas.itemconfigure(text, text='')


def move_planet(planet, planet_radius, angle, distance_to_sun, speed):
    angle += speed
    planet_x = sun_x + distance_to_sun * math.cos(angle)
    planet_y = sun_y + distance_to_sun * math.sin(angle)
    canvas.coords(planet,
                  planet_x - planet_radius,
                  planet_y - planet_radius,
                  planet_x + planet_radius,
                  planet_y + planet_radius)
    window.after(10, move_planet, planet, planet_radius,
                 angle, distance_to_sun, speed)


def start_simulation():
    for planet in planets:
        orbit = planet['orbit']
        size = planet['size']
        color = planet['color']
        speed = planet['speed']
        planet_x = sun_x + orbit/2
        planet_y = sun_y
        oval = canvas.create_oval(
            planet_x - size/2,
            planet_y - size/2,
            planet_x + size/2,
            planet_y + size/2,
            fill=color, width=0
        )
        canvas.tag_bind(oval, '<Enter>', show_info)
        canvas.tag_bind(oval, '<Leave>', hide_info)
        shape2planet[oval] = planet
        print(f'binding: {oval}')
        move_planet(oval, size/2, 0, orbit/2, speed)


def draw_text():
    global text
    text = canvas.create_text(
        200, 430, font=('Orbitron', 12), width=300, justify='center', text='', fill='gray70')


def setup_window():
    # Create the main window
    window = tk.Tk()
    window.title('Solar System')
    window.resizable(False, False)


def setup_canvas():
    # Create a canvas widget
    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg='gray15')
    # Pack the canvas widget into the main window
    canvas.pack()


# 1. setup game window
setup_window()

# 2. create and place canvas
setup_canvas()


load_planets()
draw_text()
draw_sun()
draw_orbits()


start_simulation()

# Run the main event loop
window.mainloop()
