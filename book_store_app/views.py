from rest_framework.views import APIView
from .models import Book, Author, Publisher, Genre
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, PublisherSerializer
from rest_framework.response import Response

class BookList(APIView):
    
    def get(self, request, format=None):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    
class AuthorList(APIView):
    def get(self, request, format=None):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)
    
class GenreList(APIView):
    def get(self, request, format=None):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
    
class PublisherList(APIView):
    def get(self, request, format=None):
        publisher = Publisher.objects.all()
        serializer = PublisherSerializer(publisher, many=True)
        return Response(serializer.data)