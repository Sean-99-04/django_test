from django.db import models

# Create your models here.
class MyObject(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title