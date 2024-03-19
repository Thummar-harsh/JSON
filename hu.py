import json
value = "Professional JavaScript"

with open('data.json', 'r') as file:
    data = json.load(file)
   
    books = data.get("books", [])
    print(books)
    selected_books = []

    for book in books:
        if book.get("title") == value:
            selected_books.append(book)
            # print(book)
 