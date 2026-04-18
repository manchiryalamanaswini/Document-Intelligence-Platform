from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books),
    path('upload/', views.upload_books),
    path('ask/', views.ask_question),
    path('recommend/<int:book_id>/', views.recommend_books),
]