# Notes:
# https://www.notion.so/6-Ask-the-Expert-b19271c75b0047c991b05a4f95da0bd4

from tkinter import Tk, simpledialog, messagebox

the_world = {
    'Canada': 'Ottawa',
    'China': 'Beijing',
    'France': 'Paris',
    'Egypt': 'Cairo',
    'Germany': 'Berlin',
    'UK': 'London'
}

# window = Tk()
# window.mainloop()

while True:
    # country = input("Type the name of a country:")
    country = simpledialog.askstring('Country', 'Type the name of a country:')

    if country is not None:
        if country in the_world:
            result = the_world[country]
            # print(f'The capital of {country} is {result}')
            messagebox.showinfo('Answer',
                                'The capital of ' + country + ' is ' + result)
        else:
            # city = input("Can you tell me the capital of " + country + "?")
            city = simpledialog.askstring(
                'Teach me',
                'Can you tell me the capital city of ' + country + '?')
            if city is not None:
                the_world[country] = city
