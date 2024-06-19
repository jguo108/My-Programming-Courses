# https://projects.raspberrypi.org/en/projects/solar-system-simulator/0
# https://www.freepik.com/free-vector/classic-solar-system-scheme-with-flat-deisgn_2899001.htm#fromView=search&page=1&position=0&uuid=d19eabad-53fe-4dc5-9762-7d874bd0a5f3
# https://www.freepik.com/free-vector/colorful-solar-system-scheme-with-flat-design_2880091.htm#fromView=search&page=1&position=2&uuid=d19eabad-53fe-4dc5-9762-7d874bd0a5f3
# https://www.freepik.com/free-vector/classic-solar-system-scheme-with-flat-design_2917720.htm#fromView=search&page=1&position=10&uuid=d19eabad-53fe-4dc5-9762-7d874bd0a5f3
# https://www.freepik.com/free-vector/classic-solar-system-scheme-with-flat-design_2985040.htm#fromView=search&page=1&position=18&uuid=d19eabad-53fe-4dc5-9762-7d874bd0a5f3
import tkinter as tk
import math

# TODO:
# - when user click a planet, display its info
# - add venus and earth
# - use pretty images for sun and planets
# - read planet infos from csv file

WIDTH = 400
HEIGHT = 400
planets = []
sun_x = WIDTH/2
sun_y = HEIGHT/2


def draw_sun():
    canvas.create_oval(
        sun_x - 50, sun_y - 50, sun_x + 50, sun_y + 50, fill="yellow")


def load_planets():
    info = {
        'name': 'Mercury',
        'color': 'saddle brown',
        'size': 16,
        'orbit': 150,
        'speed': 0.01,
        'info': 'The smallest and fastest planet'
    }

    image = tk.PhotoImage(file='./Resources/solar_system/mercury.png')
    canvas.create_image(0, 0, image=image, anchor='center')
    print(f'width: {image.width()}, height: {image.height()}')

    planets.append([info, image])

    info = {
        'name': 'Venus',
        'color': 'sandy brown',
        'size': 30,
        'orbit': 200,
        'speed': 0.0075,
        'info': 'The hottest planet in the Solar System. Water would turn to steam and some metals would melt just by being there!'
    }
    image = tk.PhotoImage(file='./Resources/solar_system/earth.png')
    canvas.create_image(0, 0, image=image, anchor='center')
    print(f'width: {image.width()}, height: {image.height()}')

    info = {
        'name': 'Earth',
        'color': 'deep sky blue',
        'size': 35,
        'orbit': 300,
        'speed': 0.005,
        'info': 'You are here - the only planet we know of that can support life!'
    }


def draw_orbits():
    for planet in planets:
        orbit_size = planet[0]['orbit']
        canvas.create_oval(
            (WIDTH-orbit_size)/2,
            (HEIGHT-orbit_size)/2,
            (WIDTH+orbit_size)/2,
            (HEIGHT+orbit_size)/2,
            outline="white")


def planet_clicked(event):
    print(event)


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


def create_planet(planet):
    info = planet[0]
    color = info['color']
    orbit = info['orbit']
    size = info['size']
    speed = info['speed']
    info = info['info']

    '''
    image = tk.PhotoImage(file='./Resources/solar_system/mercury.png')
    print(image)
    anvas.create_image(0, 0, image=image, anchor='center')
    print('hello')

    angle = 0
    distance_to_sun = orbit/2
    planet_x = sun_x + distance_to_sun * math.cos(angle)
    planet_y = sun_y + distance_to_sun * math.sin(angle)
    planet = canvas.create_oval(
        planet_x - size/2,
        planet_y - size/2,
        planet_x + size/2,
        planet_y + size/2,
        fill=color,
    )
    canvas.tag_bind(planet, '<Button-1>', planet_clicked)

    move_planet(planet, size/2, angle, distance_to_sun, speed)
    '''


def start_simulation():
    for planet in planets:
        create_planet(planet)


    # Create the main window
window = tk.Tk()

# Set the window size
window.geometry("400x400")

# Create a canvas widget
canvas = tk.Canvas(window, width=400, height=400, bg='black')

# Pack the canvas widget into the main window
canvas.pack()


draw_sun()
load_planets()
draw_orbits()
start_simulation()

# image = tk.PhotoImage(file='./Resources/solar_system/mercury.png')
# image = image.subsample(16, 16)
# canvas.create_image(100, 100, image=image, anchor='center')

# Run the main event loop
window.mainloop()
