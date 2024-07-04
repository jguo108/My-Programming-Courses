# Notes:
# https://www.notion.so/7-My-Book-Shelf-6a983484395647ce988b1cec5e2f966b

# Create an empty dictionary for books
books = {}


def add_book():
    title = input("Enter book title: ")
    genre = input("Enter book genre: ")
    year = int(input("Enter year of release: "))
    author = input("Enter main author: ")
    book_details = {"genre": genre, "year": year, "author": author}
    books.update({title: book_details})


def find_book():
    title = input("Enter book title to find: ")

    book_info = books.get(title)
    if book_info:
        print(f"Title: {title}")
        print(f"  Genre: {book_info['genre']}")
        print(f"  Year: {book_info['year']}")
        print(f"  Main Author: {book_info['author']}")
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
        for title, details in books.items():
            print(
                f"  - {title} ({details['genre']}, {details['year']}, {details['author']})")
    elif choice == 5:
        return
    else:
        print("Invalid choice.")


def list_books_by(criteria, value):
    print(f"All books with {criteria} '{value}':")

    for title, details in books.items():
        if details[criteria] == value:
            print(
                f"  - {title} ({details['genre']}, {details['year']}, {details['author']})")


while True:
    choice = int(input("Do you want to (1)add, (2)find, (3)list or (4)exit? "))
    if choice == 1:
        add_book()
    elif choice == 2:
        find_book()
    elif choice == 3:
        list_books()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
