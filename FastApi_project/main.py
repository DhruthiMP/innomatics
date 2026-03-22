# Day 1

# Create main.py. 
# Import FastAPI, create app = FastAPI(). 
# Add GET / that returns {\'message\': \'Welcome to City Public Library\'}.

from fastapi import FastAPI

app = FastAPI()

# -------------------- ROOT API --------------------

@app.get("/")
def home():
    return {"message": "Welcome to City Public Library"}

# Create a books list with at least 6 books. 
# Each book: id, title, author, genre (Fiction/Science/History/Tech), is_available (bool).
# Build GET /books returning all books, total count, and available_count.


# -------------------- BOOKS DATA --------------------

books = [
    {"id": 1, "title": "Python Basics", "author": "Ravi", "genre": "Tech", "is_available": True},
    {"id": 2, "title": "World History", "author": "Anita", "genre": "History", "is_available": True},
    {"id": 3, "title": "Space Science", "author": "Kiran", "genre": "Science", "is_available": False},
    {"id": 4, "title": "Mystery Island", "author": "Suresh", "genre": "Fiction", "is_available": True},
    {"id": 5, "title": "AI Revolution", "author": "Neha", "genre": "Tech", "is_available": False},
    {"id": 6, "title": "Ancient Civilizations", "author": "Arjun", "genre": "History", "is_available": True}
]

# -------------------- GET BOOKS API --------------------

@app.get("/books")
def get_books():
    
    total_count = len(books)
    
    available_count = sum(1 for book in books if book["is_available"])
    
    return {
        "total_books": total_count,
        "available_books": available_count,
        "books": books
    }

# Build GET /books/{book_id}. 
# Return the book if found, or {\'error\': \'Book not found\'} if not.
# Test with a valid and an invalid ID.

# -------------------- GET BOOK BY ID API --------------------

@app.get("/books/{book_id}")
def get_book(book_id: int):
    
    for book in books:
        if book["id"] == book_id:
            return book

    return {"error": "Book not found"}

# Create borrow_records = [] and record_counter = 1.
# Build GET /borrow-records returning all borrow records and a total count.

# -------------------- BORROW DATA --------------------

borrow_records = []
record_counter = 1

# -------------------- GET BORROW RECORDS --------------------

@app.get("/borrow-records")
def get_borrow_records():
    return {
        "total_records": len(borrow_records),
        "records": borrow_records
    }

# Build GET /books/summary (above /books/{book_id}).
# Return: total books, available count, borrowed count, and a breakdown of books per genre as a dict like {\'Fiction\': 2, \'Tech\': 3}.

# -------------------- BOOKS SUMMARY API --------------------

@app.get("/books/summary")
def get_books_summary():
    
    total_books = len(books)
    
    available_count = sum(1 for book in books if book["is_available"])
    
    borrowed_count = total_books - available_count

    genre_count = {}
    
    for book in books:
        genre = book["genre"]
        
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1

    return {
        "total_books": total_books,
        "available_books": available_count,
        "borrowed_books": borrowed_count,
        "genre_distribution": genre_count
    }

