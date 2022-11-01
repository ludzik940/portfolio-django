from django.db import models

from .validators import validate_file_size

# Create your models here.

class Links(models.Model):
    title = models.CharField(max_length = 30)
    desc = models.CharField(max_length = 300)
    link_redirect = models.CharField(max_length = 100)

    class Tag(models.TextChoices):
        PYTHON = '1', 'Python'
        MEDIA = '2', 'Media'
        YOUTUBE = '3', 'YouTube'
        COURSES = '4', 'Courses'
    
    tag = models.CharField(
        max_length= 10,
        choices = Tag.choices,
        default = Tag.PYTHON
    )

    authorized = models.BooleanField(default = False)
    

    img = models.ImageField(upload_to = 'core/static/links', max_length=100, default='/static/img/bg-try.jpg', validators=[validate_file_size])

    def __str__(self):
        return self.title

