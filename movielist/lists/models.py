from django.db import models


class Movie(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    url = models.CharField(max_length=1000, null=True)
    imdb_code = models.CharField(max_length=9, null=True)
    title = models.CharField(max_length=100, null=True)
    title_english = models.CharField(max_length=100, null=True)
    title_long = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=4, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    runtime = models.IntegerField(default=0)
    genres = models.CharField(max_length=100)
    summary = models.CharField(max_length=3000)
    description_full = models.CharField(max_length=3000, null=True)
    synopsis = models.CharField(max_length=3000, null=True)
    yt_trailer_code = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=50, null=True)
    mpa_rating = models.CharField(max_length=10, null=True)
    background_image = models.CharField(max_length=200, null=True)
    background_image_original = models.CharField(max_length=200, null=True)
    small_cover_image = models.CharField(max_length=200, null=True)
    medium_cover_image = models.CharField(max_length=200, null=True)
    large_cover_image = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=10, null=True)
    torrents = models.CharField(max_length=200, null=True)
    date_uploaded = models.DateTimeField(auto_now=True)
    date_uploaded_unix = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "Movie"
