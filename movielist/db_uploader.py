import csv
import os
import django
import sys
import rest_framework

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movielist.settings")
django.setup()

from lists.models import *

CSV_PATH = './result.csv'

with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Movie.objects.create(
            id=row['id'],
            url=row['url'],
            imdb_code=row['imdb_code'],
            title=row['title'],
            title_english=row['title_english'],
            title_long=row['title_long'],
            slug=row['slug'],
            year=row['year'],
            rating=row['rating'],
            runtime=row['runtime'],
            genres=row['genres'],
            summary=row['summary'],
            description_full=row['description_full'],
            synopsis=row['synopsis'],
            yt_trailer_code=row['yt_trailer_code'],
            language=row['language'],
            mpa_rating=['row'],
            background_image=row['background_image'],
            background_image_original=row['background_image_original'],
            small_cover_image=row['small_cover_image'],
            medium_cover_image=row['medium_cover_image'],
            large_cover_image=row['large_cover_image'],
            state=row['state'],
            torrents=row['torrents'],
            date_uploaded=row['date_uploaded'],
            date_uploaded_unix=row['date_uploaded_unix']
        )
