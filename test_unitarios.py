import unittest

class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Configura el entorno de prueba antes de cada test."""
        self.library = Library()
        self.book1 = Book("El Principito", "Antoine de Saint-Exupéry", "1234567890")
        self.book2 = Book("Cien Años de Soledad", "Gabriel García Márquez", "0987654321")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        """Prueba que se puede añadir un libro a la colección."""
        book = Book("1984", "George Orwell", "1122334455")
        self.library.add_book(book)
        self.assertIn(book, self.library.books)

    def test_find_book_by_title(self):
        """Prueba que se puede encontrar un libro por su título."""
        book = self.library.find_book_by_title("El Principito")
        self.assertEqual(book, self.book1)

    def test_update_book(self):
        """Prueba que se puede actualizar la información de un libro."""
        self.library.update_book("1234567890", "El Principito (Nuevo)", "Antoine de Saint-Exupéry (Nuevo)")
        book = self.library.find_book_by_title("El Principito (Nuevo)")
        self.assertEqual(book.title, "El Principito (Nuevo)")
        self.assertEqual(book.author, "Antoine de Saint-Exupéry (Nuevo)")

    def test_remove_book(self):
        """Prueba que se puede eliminar un libro de la colección."""
        self.library.remove_book("0987654321")
        book = self.library.find_book_by_title("Cien Años de Soledad")
        self.assertIsNone(book)

    def test_save_and_load(self):
        """Prueba que se puede guardar y cargar la colección de libros."""
        filename = "test_books.json"
        self.library.save_to_file(filename)
        new_library = Library()
        new_library.load_from_file(filename)
        self.assertEqual(len(new_library.books), 2)
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
