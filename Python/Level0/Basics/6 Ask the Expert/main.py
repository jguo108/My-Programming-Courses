

world = {}

file = open("6 Ask the Expert/world.txt", "r")
content = file.read()
file.close()
lines = content.splitlines()
for line in lines:
    pair = line.split(",")
    country = pair[0]
    capital = pair[1]
    world[country] = capital

file = open("6 Ask the Expert/world.txt", "a")

while True:
    choice = input("Do you want to(1) learn about capitals or (2) quit?")

    if choice == "1":
        country = input("Type the name of a country:")

        if country.lower() in world:
            capital = world[country.lower()]
            print(f"The capital of {country} is {capital}.")
        else:
            capital = input(
                f"I do not know the capital of {country}. Could you tell me?")
            world[country] = capital
            file.write(f"{country},{capital}")
            file.write("\n")
            file.flush()
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.")

file.close()
