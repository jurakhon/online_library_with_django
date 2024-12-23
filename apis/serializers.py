from rest_framework import serializers
from library.models import Author, Publisher, Genre, Book, Borrow


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.fullname
        representation['publisher'] = instance.publisher.name
        # representation['genres'] = instance.genres
        return representation
    class Meta:
        model = Book
        fields = ('title','author','publication_date','publisher','description','image','genres','quantity','created_at','updated_at')

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'


class BorrowSerializerbyBookID(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'

