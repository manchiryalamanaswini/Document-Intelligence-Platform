# 📚 Document Intelligence Platform

## 🚀 Overview

This project is a full-stack AI-powered web application that processes book data and enables intelligent querying using a simple RAG (Retrieval-Augmented Generation) pipeline.

---

## ⚙️ Tech Stack

* Backend: Django REST Framework (Python)
* Database: MySQL
* AI Logic: Custom Python functions (extendable to OpenAI/LM Studio)
* Automation: (Optional Selenium support)

---

## 🛠️ Setup Instructions

```bash
git clone <your-repo-link>
cd book_ai_project

# create virtual environment
python -m venv venv
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run server
python manage.py runserver
```

---

## 📡 API Endpoints

### 🔹 GET All Books

```
/api/books/
```

---

### 🔹 Upload Book (POST)

```
/api/upload/
```

Sample Input:

```json
{
  "title": "Pride and Prejudice",
  "author": "Jane Austen",
  "description": "A romantic love story",
  "rating": 4.5,
  "url": "https://example.com/book"
}
```

---

### 🔹 Ask Questions (RAG)

```
/api/ask/
```

Sample:

```json
{
  "question": "What is this book about?"
}
```

---

### 🔹 Recommend Books

```
/api/recommend/<book_id>/
```

---

## 🤖 AI Features

* Summary Generation
* Genre Classification
* Question Answering (RAG-based)
* Book Recommendations (based on genre)

---

## 🧪 Sample Outputs

### ✅ Q&A

```
Q: What is this book about?
A: This book is about: A romantic love story
```

---

### ✅ Recommendation

```
Selected Book: Pride and Prejudice  
Recommendations: Romeo and Juliet
```

---

## 📸 Screenshots

(Add screenshots like below)

```
screenshots/books.png
screenshots/upload.png
screenshots/ask.png
screenshots/recommend.png
```

---

## 📌 Notes

* The system uses a simple RAG pipeline (context-based answering)
* Can be extended with FAISS / ChromaDB for real vector search
* Designed for scalability and AI integration

---

## 👩‍💻 Author

Manaswini
