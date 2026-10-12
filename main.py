from custom_classes import MediaItem, Book, DVD, LibraryCollection

book = MediaItem("Harry Potter", "J.K. Rowling", 223)
movie = MediaItem("Insidious", "James Wan", 97)


print(book)
print(movie)

print(book.checkout())
print(book)

print(book.checkout())

dvd = DVD("Interstellar", "Christopher Nolan", 169)
print(dvd)
print(dvd.checkout())
print(dvd)
print(dvd.checkout())

library = LibraryCollection()
library.add_item(Book("Dune", "Frank Herbert", 412))
library.add_item(Book("The Hobbit", "J.R.R. Tolkien", 310))
library.add_item(DVD("The Matrix", "Wachowskis", 136))
library.add_item(MediaItem("National Geographic", "NatGeo"))

print(library.list_available())

library.items[0].checkout()
library.items[2].checkout()

print(library.list_available())