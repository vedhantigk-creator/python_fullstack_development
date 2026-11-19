
from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    # Model - Database structure
    # Views - Application logic
    # Template - HTML User Interface
    # URL - Connects browser requests to views#these are the orm operations
    #retrive the students by name
    #count total students
    #update the students's age
    