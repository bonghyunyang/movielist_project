from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=5)
    url = serializers.CharField(max_length=1000)
    imdb_code = serializers.CharField(max_length=9)
    title = serializers.CharField(max_length=100)
    title_english = serializers.CharField(max_length=100)
    title_long = serializers.CharField(max_length=200)
    slug = serializers.CharField(max_length=200)
    year = serializers.CharField(max_length=4)
    rating = serializers.DecimalField(
        max_digits=2, decimal_places=1)
    runtime = serializers.IntegerField(default=0)
    genres = serializers.CharField(max_length=100)
    summary = serializers.CharField(max_length=3000)
    description_full = serializers.CharField(max_length=3000)
    synopsis = serializers.CharField(max_length=3000)
    yt_trailer_code = serializers.CharField(max_length=100)
    language = serializers.CharField(max_length=50)
    mpa_rating = serializers.CharField(max_length=10)
    background_image = serializers.CharField(max_length=200)
    background_image_original = serializers.CharField(
        max_length=200)
    small_cover_image = serializers.CharField(max_length=200)
    medium_cover_image = serializers.CharField(max_length=200)
    large_cover_image = serializers.CharField(max_length=200)
    state = serializers.CharField(max_length=10)
    torrents = serializers.CharField(max_length=200)
    date_uploaded = serializers.DateTimeField()
    date_uploaded_unix = serializers.IntegerField(default=0)
