import json

def add_book_to_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        books = data.get("books", [])

        title = input("Enter the title of the book: ")
        authors = input("Enter the author(s) of the book (comma-separated): ").split(",")
        while True:
            try:
                edition = int(input("Enter the edition of the book: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        year = int(input("Enter the publication year of the book: "))

        new_book = {
            "title": title,
            "authors": [author.strip() for author in authors],
            "edition": edition,
            "year": year
        }

        for book in books:
            if book["authors"] == new_book["authors"] and book["edition"] == new_book["edition"]:
                print(f"Error: Book with title '{new_book['title']}' already exists with the same edition.")
                return

        books.append(new_book)
        data["books"] = books

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"Book '{new_book['title']}' successfully added to '{filename}'.")


def read_books_from_json(filename, criterion):
    with open(filename, 'r') as file:
        data = json.load(file)
        books = data.get("books", [])
        selected_books = []

        value = input(f"Enter the '{criterion}' to search: ")

        unique_authors = set()  # Set to store unique author names
        total_editions = 0

        for book in books:
            if criterion == "title" and book.get("title") == value:
                selected_books.append(book)
                unique_authors.update(book.get("authors", []))
                total_editions += 1
            elif criterion == "authors" and value in book.get("authors", []):
                selected_books.append(book)
                unique_authors.update(book.get("authors", []))
                total_editions += 1
            elif criterion == "year" and book.get("year") == int(value):
                selected_books.append(book)
                unique_authors.update(book.get("authors", []))
                total_editions += 1

        total_authors = len(unique_authors)  # Count of unique authors

        return selected_books, total_authors,total_editions
    
def remove_book_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        books = data.get("books", [])

    title = input("Enter the title of the book you want to remove: ")
    edition = input("Enter the edition of the book you want to remove: ")

    for book in books:
        if book["title"] == title and str(book["edition"]) == edition:
            books.remove(book)
            print(f"Book '{title}' (Edition: {edition}) successfully removed.")
            break
    else:
        print(f"Book '{title}' (Edition: {edition}) not found.")

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    while True:
        n = int(input("Enter 1 to add a book & 2 to read a book, 3 to remove a book, or any other number to quit: "))
        if n == 1:
            add_book_to_json("data.json")
        elif n == 3:
            remove_book_from_json("data.json")
        elif n == 2:
            criterion = input("Enter the criterion (title/authors/year): ").lower()
            book_details, total_authors,total_editions = read_books_from_json("data.json", criterion)
            if book_details:
                print("Book Details:")
                if total_authors > 1:
                  print(f"Total Authors: {total_authors}")
                if len(book_details) > 1:
                    print(f"Total Editions of the book: {total_editions}")
                for book in book_details:
                    print(f"Title: {book['title']}")
                    print(f"Authors: {', '.join(book['authors'])}")
                    print(f"Edition: {book['edition']}")
                    print(f"Year: {book['year']}")
                    print("___________________________________")
            else:
                print("No book found based on the given criterion.")
        else:
            print("Exiting...")
            break


main()
