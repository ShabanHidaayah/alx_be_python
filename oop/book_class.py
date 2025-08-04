class Book:
    """A class representing a book with title, author, and publication year."""

    def __init__(self, title: str, author: str, year: int):
        """Initialize a Book instance with title, author, and year.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when the Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """Return an informal string representation of the Book.
        
        Returns:
            str: A string in the format "title by author, published in year".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Return an official string representation that can recreate the Book instance.
        
        Returns:
            str: A string in the format "Book('title', 'author', year)".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
