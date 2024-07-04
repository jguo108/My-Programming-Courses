# Notes:
# https://www.notion.so/7-My-Book-Shelf-6a983484395647ce988b1cec5e2f966b

# Create an empty dictionary for books
books = {}


def load_books():
    pass


def save_books():
    pass


def print_book(title, info):
    print(f"Title: {title}")
    print(f"  Genre: {info['genre']}")
    print(f"  Year: {info['year']}")
    print(f"  Main Author: {info['author']}")


def add_book():
    title = input('Enter book title: ')
    genre = input('Enter book genre: ')
    year = input('Enter year of release: ')
    author = input('Enter main author: ')
    info = {'genre': genre, 'year': year, 'author': author}
    books.update({title: info})


def find_books():
    keyword = input('Enter keyword of book title to find: ')

    matching_titles = []
    for title in books.keys():
        if keyword in title:
            matching_titles.append(title)

    for title in matching_titles:
        book_info = books.get(title)
        if book_info:
            print_book(title, info)
        else:
            print(f"book '{title}' not found.")


def list_books():
    choice = int(
        input("Do you want to list books by (1)genre, (2)year, (3)author, (4)all or (5)exit? "))

    if choice == 1:
        genre = input("Enter genre: ")
        list_books_by('genre', genre)
    elif choice == 2:
        year = input("Enter year: ")
        list_books_by('year', year)
    elif choice == 3:
        author = input("Enter author: ")
        list_books_by('author', author)
    elif choice == 4:
        print("All books:")
        for title, info in books.items():
            print_book(title, info)
    elif choice == 5:
        return
    else:
        print("Invalid choice.")


def list_books_by(criteria, value):
    print(f"All books with {criteria} '{value}':")

    for title, info in books.items():
        if info[criteria] == value:
            print_book(title, info)


load_books()

while True:
    choice = int(input("Do you want to (1)add, (2)find, (3)list or (4)exit? "))
    if choice == 1:
        add_book()
    elif choice == 2:
        find_books()
    elif choice == 3:
        list_books()
    elif choice == 4:
        save_books()
        break
    else:
        print("Invalid choice. Please try again.")
