from django.db import models

# Create your models here.
from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField(max_length=20)
    slug = models.SlugField(max_length=20)

    def __str__(self):
        return f'{self.id};' \
               f'{self.name};' \
               f'{self.price};' \
               f'{self.image};' \
               f'{self.release_date};' \
               f'{self.lte_exists};' \
               f'{self.slug};'