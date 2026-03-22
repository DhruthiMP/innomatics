# -------------------- IMPORTS --------------------
from fastapi import FastAPI, Query, status
from pydantic import BaseModel, Field
from typing import Optional
import math

app = FastAPI()

# -------------------- DATA --------------------
# Day 1 — Initial in-memory database

books = [
    {"id": 1, "title": "Python Basics", "author": "Ravi", "genre": "Tech", "is_available": True},
    {"id": 2, "title": "History of India", "author": "Anita", "genre": "History", "is_available": True},
    {"id": 3, "title": "AI Revolution", "author": "Kiran", "genre": "Science", "is_available": False},
    {"id": 4, "title": "Fiction World", "author": "Suresh", "genre": "Fiction", "is_available": True},
    {"id": 5, "title": "Data Science", "author": "Meena", "genre": "Tech", "is_available": True},
    {"id": 6, "title": "Space Science", "author": "Arjun", "genre": "Science", "is_available": False},
]

borrow_records = []
record_counter = 1
queue = []

# -------------------- HELPERS --------------------
# Day 2 — Helper functions

def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

# Premium users can borrow up to 60 days
# Regular users up to 30 days
def calculate_due_date(days, member_type="regular"):
    if member_type == "premium":
        return f"Return by: Day {15 + min(days, 60)}"
    return f"Return by: Day {15 + min(days, 30)}"

# Filter helper
def filter_books_logic(genre=None, author=None, is_available=None):
    result = books

    if genre is not None:
        result = [b for b in result if b["genre"].lower() == genre.lower()]

    if author is not None:
        result = [b for b in result if b["author"].lower() == author.lower()]

    if is_available is not None:
        result = [b for b in result if b["is_available"] == is_available]

    return result

# -------------------- MODELS --------------------
# Day 2 — Request validation

class BorrowRequest(BaseModel):
    member_name: str = Field(min_length=2)
    book_id: int = Field(gt=0)
    borrow_days: int = Field(gt=0, le=60)
    member_id: str = Field(min_length=4)
    member_type: str = "regular"

class NewBook(BaseModel):
    title: str = Field(min_length=2)
    author: str = Field(min_length=2)
    genre: str = Field(min_length=2)
    is_available: bool = True

# -------------------- DAY 1 APIs --------------------

@app.get("/")
def home():
    return {"message": "Welcome to City Public Library"}

@app.get("/books")
def get_books():
    available = sum(1 for b in books if b["is_available"])
    return {
        "total": len(books),
        "available_count": available,
        "books": books
    }

@app.get("/books/summary")
def summary():
    genres = {}
    for b in books:
        genres[b["genre"]] = genres.get(b["genre"], 0) + 1

    available = sum(1 for b in books if b["is_available"])

    return {
        "total": len(books),
        "available": available,
        "borrowed": len(books) - available,
        "genres": genres
    }

@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = find_book(book_id)
    if not book:
        return {"error": "Book not found"}
    return book

@app.get("/borrow-records")
def get_records():
    return {"total": len(borrow_records), "records": borrow_records}

# -------------------- DAY 2 & 3 --------------------

@app.post("/borrow")
def borrow_book(req: BorrowRequest):
    global record_counter

    book = find_book(req.book_id)

    if not book:
        return {"error": "Book not found"}

    if not book["is_available"]:
        return {"error": "Book already borrowed"}

    book["is_available"] = False

    record = {
        "record_id": record_counter,
        "member_name": req.member_name,
        "member_id": req.member_id,
        "member_type": req.member_type,
        "book_id": req.book_id,
        "due": calculate_due_date(req.borrow_days, req.member_type)
    }

    borrow_records.append(record)
    record_counter += 1

    return record

@app.get("/books/filter")
def filter_books(
    genre: Optional[str] = None,
    author: Optional[str] = None,
    is_available: Optional[bool] = None
):
    result = filter_books_logic(genre, author, is_available)
    return {"count": len(result), "books": result}

# -------------------- DAY 4 CRUD --------------------

@app.post("/books", status_code=status.HTTP_201_CREATED)
def add_book(book: NewBook):

    for b in books:
        if b["title"].lower() == book.title.lower():
            return {"error": "Duplicate title"}

    new = book.dict()
    new["id"] = len(books) + 1
    books.append(new)

    return new

@app.put("/books/{book_id}")
def update_book(book_id: int, genre: Optional[str] = None, is_available: Optional[bool] = None):

    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    if genre is not None:
        book["genre"] = genre

    if is_available is not None:
        book["is_available"] = is_available

    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    books.remove(book)

    return {"message": f"{book['title']} deleted"}

# -------------------- DAY 5 WORKFLOW --------------------

@app.post("/queue/add")
def add_queue(member_name: str, book_id: int):

    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    if book["is_available"]:
        return {"message": "Book is available, no need to queue"}

    queue.append({"member_name": member_name, "book_id": book_id})

    return {"message": "Added to queue"}

@app.get("/queue")
def get_queue():
    return queue

@app.post("/return/{book_id}")
def return_book(book_id: int):
    global record_counter

    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    book["is_available"] = True

    for q in queue:
        if q["book_id"] == book_id:

            book["is_available"] = False

            record = {
                "record_id": record_counter,
                "member_name": q["member_name"],
                "book_id": book_id,
                "due": calculate_due_date(10)
            }

            borrow_records.append(record)
            queue.remove(q)
            record_counter += 1

            return {"message": "returned and re-assigned", "record": record}

    return {"message": "returned and available"}

# -------------------- DAY 6 SEARCH / SORT / PAGINATION --------------------

@app.get("/books/search")
def search_books(keyword: str):

    result = [
        b for b in books
        if keyword.lower() in b["title"].lower()
        or keyword.lower() in b["author"].lower()
    ]

    return {"total_found": len(result), "results": result}

@app.get("/books/sort")
def sort_books(sort_by: str = "title", order: str = "asc"):

    if sort_by not in ["title", "author", "genre"]:
        return {"error": "Invalid sort_by"}

    if order not in ["asc", "desc"]:
        return {"error": "Invalid order"}

    reverse = order == "desc"

    sorted_books = sorted(
        books,
        key=lambda x: x[sort_by].lower(),
        reverse=reverse
    )

    return {"sorted_by": sort_by, "order": order, "books": sorted_books}

@app.get("/books/page")
def paginate(page: int = 1, limit: int = 3):

    total = len(books)
    start = (page - 1) * limit
    end = start + limit

    return {
        "total": total,
        "total_pages": math.ceil(total / limit),
        "page": page,
        "limit": limit,
        "books": books[start:end]
    }

@app.get("/borrow-records/search")
def search_records(member_name: str):

    result = [
        r for r in borrow_records
        if member_name.lower() in r["member_name"].lower()
    ]

    return {"results": result}

@app.get("/borrow-records/page")
def paginate_records(page: int = 1, limit: int = 2):

    total = len(borrow_records)
    start = (page - 1) * limit
    end = start + limit

    return {
        "total": total,
        "page": page,
        "records": borrow_records[start:end]
    }

# -------------------- FINAL COMBINED BROWSE --------------------

@app.get("/books/browse")
def browse(
    keyword: Optional[str] = None,
    sort_by: str = "title",
    order: str = "asc",
    page: int = 1,
    limit: int = 3
):

    result = books

    # FILTER
    if keyword:
        result = [
            b for b in result
            if keyword.lower() in b["title"].lower()
            or keyword.lower() in b["author"].lower()
        ]

    # SORT
    reverse = order == "desc"
    result = sorted(result, key=lambda x: x[sort_by].lower(), reverse=reverse)

    # PAGINATE
    total = len(result)
    start = (page - 1) * limit
    end = start + limit

    return {
        "keyword": keyword,
        "sort_by": sort_by,
        "order": order,
        "total": total,
        "page": page,
        "results": result[start:end]
    }