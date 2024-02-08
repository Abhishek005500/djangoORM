from django.db import models

# # Create your models here.
# class Album(models.Model): 
# 	title = models.CharField(max_length = 30) 
# 	artist = models.CharField(max_length = 30) 
# 	genre = models.CharField(max_length = 30) 



# class Song(models.Model): 
# 	name = models.CharField(max_length = 100) 
# 	album = models.ForeignKey(Album, on_delete = models.CASCADE) 


# class Course(models.Model):
#     name = models.CharField(max_length = 100) 


# class Semester(models.Model):
#     name = models.CharField(max_length = 100)
        

# class Subject(models.Model):
#     name = models.CharField(max_length = 100) 
#     course = models.ManyToManyField(Course) 
#     semester = models.ManyToManyField(Semester)
    
    
from datetime import date

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    
    