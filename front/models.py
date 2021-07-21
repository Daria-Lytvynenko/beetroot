from django.db import models


# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    visible = models.BooleanField(default=True)
    order = models.IntegerField(default=100)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class News(Page):
    time_pub = models.DateTimeField()
    anounce = models.TextField()
    tags = models.ManyToManyField(Tag)


