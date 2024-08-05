

# countries = ["canada", "china", "france", "egypt", "germany", "uk"]
# capitals = ["ottawa", "beijing", "paris", "cairo", "berlin", "london"]


# world = {"china": "beijing", "germany": "berlin",
#         "france": "paris", "egypt": "cairo", "uk": "london"}

world = {}

file = open("6 Ask the Expert/world.txt", "r")
content = file.read()
file.close()
lines = content.splitlines()
# print(lines)
for line in lines:
    pair = line.split(",")
    country = pair[0]
    capital = pair[1]
    world[country] = capital

print(world)

# file = open("6 Ask the Expert/world.txt", "w")
file = open("6 Ask the Expert/world.txt", "a")

while True:
    choice = input("Do you want to(1) learn about capitals or (2) quit?")

    if choice == "1":
        country = input("Type the name of a country:")

        # if countries.count(country) != 0:
        # if country.lower() in countries:
        if country.lower() in world:
            # index = countries.index(country)
            # index = countries.index(country.lower())
            # capital = ""
            # capital = capitals[index]
            capital = world[country.lower()]
            print(f"The capital of {country} is {capital}.")
        else:
            # print(
            #   f"I do not know the capital of {country}. Could you tell me?")

            capital = input(
                f"I do not know the capital of {country}. Could you tell me?")
            # countries.append(country.lower())
            # capitals.append(capital.lower())
            world[country] = capital
            file.write(f"{country},{capital}")
            file.write("\n")
            file.flush()

        '''
        if country.lower() in countries:
            index = countries.index(country)
            capital = capitals[index]
            print(f"The capital of {country} is {capital}.")
        else:
            # print(f"I do not know the capital of {country}. Try a different one.")
            capital = input(
                f"I do not know the capital of {country}. Could you tell me?")
            if capital is not None:
                capitals.append(city)
                countries.append(country)
        '''
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.")

file.close()
