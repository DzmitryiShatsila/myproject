from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class TheoryManager(models.Manager):
    def get_queryset(self):
        # return super(TheoryManager, self).get_queryset().filter(material_type='practice')
        return super().get_queryset()


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
    objects = models.Manager()
    theory = TheoryManager()


    def get_absolute_url(self):
        return reverse('lesson:material_details',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
