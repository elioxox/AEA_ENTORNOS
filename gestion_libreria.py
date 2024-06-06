import json
import os

class Book:
    """
    Representa un libro en la librería.

    Attributes:
        title (str): El título del libro.
        author (str): El autor del libro.
        isbn (str): El ISBN del libro.
    """

    def __init__(self, title, author, isbn):
        """
        Inicializa un libro con el título, autor e ISBN proporcionados.

        Args:
            title (str): El título del libro.
            author (str): El autor del libro.
            isbn (str): El ISBN del libro.
        """
        self.title = title
        self.author = author
        self.isbn = isbn


class Library:
    """
    Clase para gestionar una colección de libros.

    Methods:
        add_book(book): Añade un libro a la colección.
        find_book_by_title(title): Busca un libro por su título.
        update_book(isbn, new_title, new_author): Actualiza la información de un libro.
        remove_book(isbn): Elimina un libro de la colección por su ISBN.
        save_to_file(filename): Guarda la colección de libros en un archivo.
        load_from_file(filename): Carga la colección de libros desde un archivo.
    """

    def __init__(self):
        """Inicializa una nueva instancia de la clase Library."""
        self.books = []

    def add_book(self, book):
        """
        Añade un libro a la colección.

        Args:
            book (Book): El libro a añadir.
        """
        self.books.append(book)

    def find_book_by_title(self, title):
        """
        Busca un libro por su título.

        Args:
            title (str): El título del libro a buscar.

        Returns:
            Book: El libro encontrado, o None si no se encuentra.
        """
        for book in self.books:
            if book.title == title:
                return book
        return None

    def update_book(self, isbn, new_title, new_author):
        """
        Actualiza la información de un libro.

        Args:
            isbn (str): El ISBN del libro a actualizar.
            new_title (str): El nuevo título del libro.
            new_author (str): El nuevo autor del libro.

        Returns:
            bool: True si el libro se actualizó
            , False si no se encontró.
        """
        for book in self.books:
            if book.isbn == isbn:
                book.title = new_title
                book.author = new_author
                return True
        return False

    def remove_book(self, isbn):
        """
        Elimina un libro de la colección por su ISBN.

        Args:
            isbn (str): El ISBN del libro a eliminar.

        Returns:
            bool: True si el libro se eliminó, False si no se encontró.
        """
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    def save_to_file(self, filename):
        """
        Guarda la colección de libros en un archivo JSON.

        Args:
            filename (str): El nombre del archivo donde se guardará la colección.
        """
        books_data = [{'title': book.title, 'author': book.author, 'isbn': book.isbn} for book in self.books]
        with open(filename, 'w') as file:
            json.dump(books_data, file)

    def load_from_file(self, filename):
        """
        Carga la colección de libros desde un archivo JSON.

        Args:
            filename (str): El nombre del archivo desde donde se cargará la colección.
        """
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                books_data = json.load(file)
                self.books = [Book(book['title'], book['author'], book['isbn']) for book in books_data]
