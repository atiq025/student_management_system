from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    COURSE_CHOICES = [
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('ENG', 'Engineering'),
        ('MATH', 'Mathematics'),
        ('BIO', 'Biology'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)

    def __str__(self):
        return self.name


