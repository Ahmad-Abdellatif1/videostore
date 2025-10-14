from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

THIS_YEAR = datetime.date.today().year

class Movie(models.Model):
    # assignment asks for MovieID explicitly
    MovieID      = models.IntegerField(primary_key=True)
    MovieTitle   = models.CharField(max_length=200)
    Actor1Name   = models.CharField(max_length=120)
    Actor2Name   = models.CharField(max_length=120, blank=True)
    DirectorName = models.CharField(max_length=120)

    GENRE_CHOICES = [
        ("COMEDY", "Comedy"),
        ("ROMANCE", "Romance"),
        ("ACTION",  "Action"),
        ("DRAMA",   "Drama"),
        ("THRILLER","Thriller"),
        ("SCIFI",   "Sci-Fi"),
        ("HORROR",  "Horror"),
        ("OTHER",   "Other"),
    ]
    MovieGenre   = models.CharField(max_length=20, choices=GENRE_CHOICES)

    ReleaseYear  = models.PositiveIntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(THIS_YEAR + 1)]
    )

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"