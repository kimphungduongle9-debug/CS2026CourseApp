from django.db import models
from django.contrib.auth.models import AbstractUser
from unicodedata import category
from ckeditor.fields import RichTextField


# Create your models here.
class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    updates_date = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True, null=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)
    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    description = RichTextField()
    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.subject


#bài học của 1 khóa học
class Lesson(BaseModel):
    subject = models.CharField(max_length=255, null = False)
    content = RichTextField()
    image = models.ImageField(upload_to='lesson/%Y/%m')
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    tags = models.ManyToManyField('Tag')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('subject', 'category')

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name