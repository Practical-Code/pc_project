from django.db import models

class Post(models.Model):
    post = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    