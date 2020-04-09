from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Material(models.Model):
    MATERIAL_TYPE = (
        ('theory', 'Theoretical material'),
        ('practice', 'Practical')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_materials')
    material_type = models.CharField(max_length=20,
                                     choices=MATERIAL_TYPE,
                                     default='theory')

    # def __str__(self):
    #     return self.title
