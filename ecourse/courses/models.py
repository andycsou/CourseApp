from django.db import models
from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField

# Create your models here.
class User(AbstractUser):
    pass

#luu y ki phan abstract nay nha

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']

class Category(BaseModel):
    name = models.CharField(max_length=180)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=100)
    # description = models.TextField(null=True)
    description = RichTextField(null=True)
    image = models.ImageField(upload_to="courses/%Y/%m")
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.subject

class Leson(BaseModel):
    subject = models.CharField(max_length=50) #id kieu in tu tang
    description = RichTextField(null=True)
    image = models.ImageField(upload_to="lessons/%Y/%m")
    tags = models.ManyToManyField('Tag')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject

class Tag(BaseModel):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name