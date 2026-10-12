from custom_classes import MediaItem, DVD

book = MediaItem("Harry Potter", "J.K. Rowling")
movie = MediaItem("Insidious", "James Wan")

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