class MediaItem:
    """A generic item in a library that can be checked out and returned."""

    def __init__(self, title, author, is_available=True):
        """Create an item with a title, an author and an availability status."""
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        """Check the item out if it is available and return a status message."""
        if self.is_available:
            self.is_available = False
            return "Successful checkout"
        return "Already out"

    def return_item(self):
        """Mark the item as available again."""
        self.is_available = True

    def __str__(self):
        """Return the item as 'Title by Author [Available/Checked Out]'."""
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} [{status}]"


class Book(MediaItem):
    """A library item that also keeps its page count."""

    def __init__(self, title, author, page_count, is_available=True):
        """Create a book with a title, an author and a page count."""
        super().__init__(title, author, is_available)
        self.page_count = page_count

    def __str__(self):
        """Return the item description followed by the page count."""
        return f"{super().__str__()} - {self.page_count} pages"


class DVD(MediaItem):
    """A library item that also keeps its duration and needs careful handling."""

    def __init__(self, title, author, duration, is_available=True):
        """Create a DVD with a title, an author and a duration in minutes."""
        super().__init__(title, author, is_available)
        self.duration = duration

    def checkout(self):
        """Check the DVD out and print a care reminder if it was successful."""
        result = super().checkout()
        # Must match the success message in MediaItem.checkout(), otherwise the reminder never prints.
        if result == "Successful checkout":
            print("Handle with care: Do not scratch the disc.")
        return result


class LibraryCollection:
    """A container that holds library items."""

    def __init__(self):
        """Create an empty collection."""
        self.items = []

    def add_item(self, item):
        """Add a MediaItem or any of its subclasses to the collection."""
        self.items.append(item)

    def list_available(self):
        """Return the titles of all items that are currently available."""
        return [item.title for item in self.items if item.is_available]