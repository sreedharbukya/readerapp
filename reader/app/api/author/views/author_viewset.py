from rest_framework import viewsets

from app.api.author.serializers.author_serializer import AuthorSerializer
from app.models.author import Author


class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
