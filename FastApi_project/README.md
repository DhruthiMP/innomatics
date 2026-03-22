# 📚 FastAPI Library Book Management System

## 🚀 Project Overview
This project is a **Library Book Management System** built using **FastAPI** as part of a FastAPI Internship Final Project.

It demonstrates real-world backend development concepts including API design, data validation, CRUD operations, and multi-step workflows.

---

## 🎯 Features

### ✅ Day 1 — GET APIs
- Home route (`/`)
- Get all books (`/books`)
- Get book by ID (`/books/{book_id}`)
- Books summary (`/books/summary`)
- Borrow records list (`/borrow-records`)

### ✅ Day 2 — POST + Pydantic
- Borrow book with validation (`/borrow`)
- Field constraints using Pydantic

### ✅ Day 3 — Helper Functions & Filtering
- Helper functions:
  - `find_book()`
  - `calculate_due_date()`
  - `filter_books_logic()`
- Filter books (`/books/filter`)

### ✅ Day 4 — CRUD Operations
- Add book (`POST /books`)
- Update book (`PUT /books/{book_id}`)
- Delete book (`DELETE /books/{book_id}`)

### ✅ Day 5 — Multi-Step Workflow
- Borrow → Return → Reassign
- Queue system:
  - Add to queue (`/queue/add`)
  - View queue (`/queue`)
  - Return & auto-assign (`/return/{book_id}`)

### ✅ Day 6 — Advanced APIs
- Search books (`/books/search`)
- Sort books (`/books/sort`)
- Pagination (`/books/page`)
- Borrow record search & pagination
- Combined browsing (`/books/browse`)

---

## 🛠️ Tech Stack
- Python 🐍
- FastAPI ⚡
- Pydantic
- Uvicorn

---

## 📂 Project Structure