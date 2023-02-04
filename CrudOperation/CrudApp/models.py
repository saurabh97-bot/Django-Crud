from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TestModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField()
    phone = models.IntegerField()
    active = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'self.name + self.text'
