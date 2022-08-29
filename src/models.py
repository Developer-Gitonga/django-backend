from django.db import models
from django.db.models import Q
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Location(models.Model):
    url = models.CharField(max_length=48)
    title = models.CharField(max_length=200)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    image = CloudinaryField()
    url = models.CharField(max_length=48)
    title = models.CharField(max_length=48)
    genus = models.CharField(max_length=200)
    caption = models.TextField(max_length=2000)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name = 'Category List'


class Cat(models.Model):
    image = CloudinaryField()
    title = models.CharField(max_length=200)
    caption = models.TextField(max_length=2000)
    posted = models.DateTimeField('date published', default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def save_cat(self):
        self.save()

    @classmethod
    def search_by_category(cls, search_term):
        cats = cls.objects.filter(Q(category__title__icontains=search_term) | Q(
            title__icontains=search_term) | Q(caption__icontains=search_term))

        return cats

    def __str__(self):
        return self.title
