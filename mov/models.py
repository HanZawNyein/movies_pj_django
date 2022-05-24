from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mov:movies_list_by_category', args=[self.name])


class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status='publish')


class Movie(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    production = models.IntegerField()
    poster = models.ImageField(upload_to="Movie/Poster/", blank=True)
    review = models.TextField()

    MOVIES_TYPE = (
        ('movie', 'Movie'),
        ('series', 'Series')
    )
    type = models.CharField(max_length=10, choices=MOVIES_TYPE)
    category = models.ManyToManyField(Category, related_name="category_of_movies")
    created = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Publish')
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  # The default manager.
    publish = PublishManager()  # Our custom manager.

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mov:movie_detail', args=[self.type, self.slug, self.production])


class MovieImage(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_of_movie_image")
    image = models.ImageField()

    def __str__(self):
        return self.movie.name


class DriveName(models.Model):
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='drive_icons/')

    def __str__(self):
        return self.name


class MovieURL(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_of_movie_url")
    drive = models.ForeignKey(DriveName, on_delete=models.RESTRICT)
    url = models.URLField()
    resolution = models.CharField(max_length=50)
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.movie.name


class SeriesURL(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_of_series_url")
    drive = models.ForeignKey(DriveName, on_delete=models.RESTRICT)
    season = models.IntegerField()
    episode = models.IntegerField()
    url = models.URLField()
    resolution = models.CharField(max_length=50)
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.movie.name
