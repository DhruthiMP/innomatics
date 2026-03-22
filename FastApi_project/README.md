# FastAPI Final Project

# Library Book Management System

This project is developed as part of the FastAPI Internship Final Project.
The goal is to build a complete real world FastAPI backend system implementing concepts from Day 1 to Day 6.

---

# Project Objective

Build a fully functional FastAPI backend system implementing:

1. GET APIs
2. POST APIs with Pydantic validation
3. Helper functions
4. CRUD operations
5. Multi step workflows
6. Search, sorting, and pagination

---

# Selected Project

1. Project Name: Library Book Management System
2. Framework: FastAPI
3. Language: Python
4. API Type: REST

---

# Project Structure

```
main.py
requirements.txt
README.md
screenshots/
```

---

# Endpoints

1. GET /
   Home route

2. GET /books
   Get all books

3. GET /books/summary
   Books summary with counts

4. GET /books/{book_id}
   Get book by ID

5. GET /borrow-records
   Get all borrow records

6. POST /borrow
   Borrow a book

7. GET /books/filter
   Filter books

8. POST /books
   Add new book

9. PUT /books/{book_id}
   Update book

10. DELETE /books/{book_id}
    Delete book

11. POST /queue/add
    Add user to queue

12. GET /queue
    View queue

13. POST /return/{book_id}
    Return book

14. GET /books/search
    Search books

15. GET /books/sort
    Sort books

16. GET /books/page
    Paginate books

17. GET /borrow-records/search
    Search borrow records

18. GET /borrow-records/page
    Paginate borrow records

19. GET /books/browse
    Combined filter sort pagination

20. GET /books/filter (with multiple parameters tested)
    Advanced filtering use case

---

# Features Implemented

1. REST API development
2. Pydantic validation
3. CRUD operations
4. Helper functions
5. Multi step workflows
6. Search functionality
7. Sorting logic
8. Pagination logic
9. Queue management
10. Borrow return workflow

---

# How to Run

1. Install dependencies

```
pip install -r requirements.txt
```

2. Run server

```
uvicorn main:app --reload
```

3. Open Swagger

```
http://127.0.0.1:8000/docs
```

---

# Testing

1. APIs tested using Swagger UI
2. Screenshots captured for all endpoints
3. Stored in screenshots folder

---

# Learning Outcomes

1. Built real world FastAPI backend
2. Implemented RESTful APIs
3. Used Pydantic validation
4. Implemented CRUD operations
5. Created multi step workflows
6. Implemented search sorting pagination
7. Structured FastAPI project

---

# Submission Checklist

1. Project implemented
2. 20 endpoints completed
3. Swagger testing done
4. Screenshots added
5. GitHub repository created
6. LinkedIn post published
7. Tagged Innomatics Research Labs
