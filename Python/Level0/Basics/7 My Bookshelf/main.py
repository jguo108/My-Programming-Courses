# Notes:
# https://www.notion.so/7-My-Book-Shelf-6a983484395647ce988b1cec5e2f966b

# Create an empty dictionary for movies
movies = {}


def add_movie(title, genre, year, actor):
    # Create a dictionary for the movie details
    movie_details = {"genre": genre, "year": year, "actor": actor}
    # Add the new movie and details to the movies dictionary
    movies.update({title: movie_details})


def find_movie(title):
    # Get the movie details using get (returns None if not found)
    movie_info = movies.get(title)
    if movie_info:
        print(f"Title: {title}")
        print(f"  Genre: {movie_info['genre']}")
        print(f"  Year: {movie_info['year']}")
        print(f"  Main Actor: {movie_info['actor']}")
    else:
        print(f"Movie '{title}' not found.")


def list_movies():
    # Loop through all movies and print details
    if not movies:
        print("No movies added yet!")
        return
    print("All Movies:")
    for title, details in movies.items():
        print(f"  - {title} ({details['genre']}, {details['year']})")


def list_movies_by_genre(genre):
    # Loop through all movies and print details if genre matches
    print(f"Movies in genre '{genre}':")
    found = False
    for title, details in movies.items():
        if details["genre"] == genre:
            print(f"  - {title}")
            found = True
    if not found:
        print("  No movies found in that genre.")


# Option to add new movies
while True:
    choice = input("Do you want to add a new movie (y/n)? ")
    if choice.lower() != 'y':
        break
    title = input("Enter movie title: ")
    genre = input("Enter movie genre: ")
    year = int(input("Enter year of release: "))
    actor = input("Enter main actor: ")
    add_movie(title, genre, year, actor)

# Option to search for movies or list all
while True:
    choice = input("What would you like to do (search/list/exit)? ")
    if choice.lower() == 'exit':
        break
    elif choice.lower() == 'search':
        title = input("Enter movie title to search: ")
        find_movie(title)
    elif choice.lower() == 'list':
        choice = input("List all movies (y/n) or by genre (enter genre)? ")
        if choice.lower() == 'y':
            list_movies()
        else:
            genre = choice
            list_movies_by_genre(genre)
    else:
        print("Invalid choice. Please try again.")
