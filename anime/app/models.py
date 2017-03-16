from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Comment(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=300)
    date = models.DateTimeField()

class Item(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    content = RichTextUploadingField(blank=True, default='')
    comments = models.ManyToManyField(Comment, blank = True)

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Chapter(models.Model): #todo
    name = models.CharField(max_length=50)
    link = models.URLField(null=True)
    number = models.IntegerField()

class Part(models.Model): #todo
    name = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)
    number = models.IntegerField()
    picture = models.ImageField(upload_to='projects/parts')
    chapters = models.ManyToManyField(Chapter, blank = True)
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='projects')
    genres = models.ManyToManyField(Genre)
    text = models.TextField()
    author = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    translation_status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    censor = models.BooleanField()
    year = models.CharField(max_length=50)   
    translator = models.CharField(max_length=50)
    cleaner = models.CharField(max_length=50)
    corrector = models.CharField(max_length=50)
    typer = models.CharField(max_length=50)
    parts = models.ManyToManyField(Part, blank = True)
    def __str__(self):
        return self.title