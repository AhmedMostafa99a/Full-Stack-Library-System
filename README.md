# 📚 Online Library Management System

A full-featured online library website built with **Django** and **Python**. Users can browse and borrow books, while admins have full control over the library's inventory.

---

## ✨ Features

### 👤 User Features
- **🔐 Sign Up / Login** with role selection (User or Admin)
- **🔍 Search** for books by title, author, or category
- **📖 View** all available books with clear availability status
- **📚 Borrow** available books with a single click
- **👀 View** a personal list of borrowed books

### ⚙️ Admin Features
- **🎯 Add, Edit, and Delete** books from the library
- **👁️ View** the complete list of available books
- **📊 Manage** the entire book inventory effortlessly

### 🌐 For Everyone
- **🚀 Dynamic Navigation Bar** that changes based on your role
- **📱 Responsive Design** accessible on all pages

---

## 🛠️ Tech Stack

- **Backend:** Django, Python
- **Database:** SQLite (default, can be configured for PostgreSQL)
- **Frontend:** HTML, CSS, JavaScript

---

## 🚀 Quick Start

1. **Clone the repo**
   ```bash
  [clone repo ](https://github.com/AhmedMostafa99a/Full-Stack-Library-System.git)
Create a virtual environment & install dependencies

bash
python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`
pip install -r requirements.txt
Run migrations & start the server

bash
python manage.py migrate
python manage.py runserver
Open your browser and go to:
http://localhost:8000
---
📦 Project Structure
text
online-library/
├── 📁 library_app/          # Main Django app
├── 📁 books/templates/            # HTML templates
├── 📁 static/CSS             # CSS, JS, and images
├── manage.py
