# Notes:
# https://www.notion.so/6-Ask-the-Expert-b19271c75b0047c991b05a4f95da0bd4

import csv

PATH = '6 Ask the Expert/world.csv'

the_world = {}

'''
the_world = {
    'Canada': 'Ottawa',
    'China': 'Beijing',
    'France': 'Paris',
    'Egypt': 'Cairo',
    'Germany': 'Berlin',
    'UK': 'London'
}
'''


def load_world(file):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            country = row[0]
            capital = row[1]
            the_world[country] = capital


def save_world(file):
    with open(file, 'w', newline='') as file:
        writer = csv.writer(file)
        for country, capital in the_world.items():
            writer.writerow([country, capital])


load_world(file=PATH)

while True:
    choice = int(input('Do you want to (1) ask the expert or (2) exit?'))

    if choice == 1:
        country = input("Type the name of a country:")

        if country is not None:
            if country in the_world:
                result = the_world[country]
                print(f'The capital of {country} is {result}')
            else:
                city = input("Can you tell me the capital of " + country + "?")
                if city is not None:
                    the_world[country.lower()] = city.lower()
    elif choice == 2:
        save_world(file=PATH)
        break
    else:
        print("Invalid choice. Please try again.")
