

countries = ["canada", "china", "france", "egypt", "germany", "uk"]
capitals = ["ottawa", "beijing", "paris", "cairo", "berlin", "london"]

while True:
    choice = input("Do you want to(1) learn about capitals or (2) quit?")

    if choice == "1":
        country = input("Type the name of a country:")

        # if countries.count(country) != 0:
        if country in countries:
            capital = ""
            print(f"The capital of {country} is {capital}.")
        else:
            print(
                f"I do not know the capital of {country}. Could you tell me?")

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
