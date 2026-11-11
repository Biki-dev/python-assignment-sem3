class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
    def calculate_late_fee(self, days_overdue):
        raise NotImplementedError("Subclass must implement this method")
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
    def calculate_late_fee(self, days_overdue):
        return max(0, days_overdue) * 2
class DVD(LibraryItem):
    def __init__(self, title, item_id, duration):
        super().__init__(title, item_id)
        self.duration = duration
    def calculate_late_fee(self, days_overdue):
        return max(0, days_overdue) * 5
book = Book("Python Programming", "B101", "John Smith")
dvd = DVD("Inception", "D101", 148)
print("Book Details:")
print("Title:", book.title) 
print("Item ID:", book.item_id)
print("Author:", book.author)
print("Late Fee: Rs.", book.calculate_late_fee(5))
print("\nDVD Details:")
print("Title:", dvd.title)
print("Item ID:", dvd.item_id)
print("Duration:", dvd.duration, "minutes")
print("Late Fee: Rs.", dvd.calculate_late_fee(5))