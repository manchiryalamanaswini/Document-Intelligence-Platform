from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from .ai_utils import generate_summary, classify_genre
from .ai_utils import answer_question

@api_view(['POST'])
def ask_question(request):
    question = request.data.get("question")

    # get latest book (you can improve later)
    book = Book.objects.last()

    if not book:
        return Response({"error": "No books available"})

    context = book.description
    answer = answer_question(question, context)

    return Response({
        "question": question,
        "answer": answer,
        "book": book.title
    })


# ✅ GET API
@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    return Response(BookSerializer(books, many=True).data)


# ✅ POST API (Upload)
@api_view(['POST'])
def upload_books(request):
    title = request.data.get("title", "No Title")
    author = request.data.get("author", "Unknown")
    description = request.data.get("description", "")
    rating = request.data.get("rating", 0)
    url = request.data.get("url", "http://example.com")

    book = Book.objects.create(
        title=title,
        author=author,
        description=description,
        rating=rating,
        url=url,
        summary=generate_summary(description),
        genre=classify_genre(description)
    )

    return Response({"message": "Book added with AI"})

@api_view(['GET'])
def recommend_books(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"})

    # find books with same genre (exclude current book)
    recommendations = Book.objects.filter(genre=book.genre).exclude(id=book.id)

    return Response({
        "selected_book": book.title,
        "genre": book.genre,
        "recommendations": BookSerializer(recommendations, many=True).data
    })