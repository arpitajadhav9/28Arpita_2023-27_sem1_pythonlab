# DESIGN A PYTHON PROGRAM TO MANAGE A LIBRARY CATALOGUE.USE  CONTROL STRUCTURES/STATEMENTS TO ADD SEARCH FOR AND CHECK OUT BOOKS AND MAINTAIN THE LIBRARY'S INVENTORY.....


books = ["The Catcher in the Rye",
    "To Kill a Mockingbird",
    "1984",
    "The Great Gatsby",
    "The Hobbit",
    "The Da Vinci Code",
    "The Alchemist",
    "The Hunger Games",
    "The Shining",
    "The Kite Runner"]


while True:
    print('\nLibrary Management System')
    print('1. Add a book')
    print('2. Display all books')
    print('3. Exit')

    choice = input('Enter your choice (1-3): ')

    if choice == '1':
        title = input('Enter the title of the book: ')
        books.append(book)
        print('Book "{title}" added successfully.')

    elif choice == '2':

            print('List of books in the library:')
            for index, book in enumerate(books, start=1):
                print('{index}.  by {book["author"]}')

    elif choice == '3':
        print('Exiting the library management system. Goodbye!')
        break

    else:
        print('Invalid choice. Please enter a number between 1 and 4.')