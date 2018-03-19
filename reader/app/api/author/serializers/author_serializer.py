from rest_framework import serializers

from app.models.author import Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Author
		fields = ('id', 'first_name', 'last_name')
