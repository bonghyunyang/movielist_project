from django.db import models

# title, year, rating, genres, summary 만 우선 추가 (DB 생성용)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    genres = models.CharField(max_length=50)
    summary = models.TextField()

    class Meta:
        db_table = "Movie"
