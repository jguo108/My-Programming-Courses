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

window = None
canvas = None

planet_infos = []
planets = []

sun_x = WIDTH/2
sun_y = 200

info_display = None


def create_sun():
    canvas.create_oval(
        sun_x - 50, sun_y - 50, sun_x + 50, sun_y + 50, fill="gold", width=0)


def create_planet(planet_info):
    orbit = planet_info['orbit']
    size = planet_info['size']
    color = planet_info['color']
    planet_x = sun_x + orbit/2
    planet_y = sun_y
    planet = canvas.create_oval(
        planet_x - size/2,
        planet_y - size/2,
        planet_x + size/2,
        planet_y + size/2,
        fill=color,
        width=0
    )
    return planet


def load_planet_infos():
    planet_info = {
        'name': 'Mercury',
        'color': 'saddle brown',
        'size': 16,
        'orbit': 150,
        'speed': 0.01,
        'info': 'The smallest and fastest planet'
    }
    planet_infos.append(planet_info)

    planet_info = {
        'name': 'Venus',
        'color': 'sandy brown',
        'size': 30,
        'orbit': 200,
        'speed': 0.0075,
        'info': 'The hottest planet in the Solar System. Water would turn to steam and some metals would melt just by being there!'
    }
    planet_infos.append(planet_info)

    planet_info = {
        'name': 'Earth',
        'color': 'deep sky blue',
        'size': 35,
        'orbit': 300,
        'speed': 0.005,
        'info': 'You are here - the only planet we know of that can support life!'
    }
    planet_infos.append(planet_info)


def create_planets():
    for planet_info in planet_infos:
        planet = create_planet(planet_info)
        planets.append(planet)


def create_orbits():
    for planet_info in planet_infos:
        orbit_size = planet_info['orbit']
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
    # canvas.itemconfigure(text, text=shape2planet[id]['info'])


def hide_info(event):
    id = event.widget.find_withtag('current')[0]
    canvas.itemconfigure(info_display, text='')


def update_info(info):
    canvas.itemconfigure(info_display, text=info)


def move_planet(planet, planet_radius, angle, distance_to_sun, speed):
    global window
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


def bind_keys():
    for planet_info, planet in zip(planet_infos, planets):
        print(planet_info['info'])
        canvas.tag_bind(planet, '<Enter>',
                        lambda event, info=planet_info['info']:
                            canvas.itemconfigure(info_display, text=info))
        canvas.tag_bind(planet, '<Leave>',
                        lambda event, info='':
                            canvas.itemconfigure(info_display, text=info))


def start_simulation():
    for planet_info, planet in zip(planet_infos, planets):
        move_planet(planet,
                    planet_info['size']/2,
                    0,
                    planet_info['orbit']/2,
                    planet_info['speed'])


def create_info_display():
    global info_display, canvas
    info_display = canvas.create_text(
        200,
        430,
        font=('Orbitron', 12),
        width=300,
        justify='center',
        text='',
        fill='gray70')


def setup_window():
    global window
    # Create the main window
    window = tk.Tk()
    window.title('Solar System')
    window.resizable(False, False)


def create_canvas():
    global window, canvas
    # Create a canvas widget
    canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg='gray15')
    # Pack the canvas widget into the main window
    canvas.pack()


def setup_gui():
    create_canvas()
    create_info_display()


# 1. setup game window
setup_window()

# 2. setup graphical user interface (GUI)
setup_gui()

# 3.
load_planet_infos()
create_sun()
create_orbits()
create_planets()

# 4.
bind_keys()

# 5.
start_simulation()

# Run the main event loop
window.mainloop()
