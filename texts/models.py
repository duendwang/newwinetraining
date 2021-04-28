from django.db import models

# Create your models here.

class Text(models:Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(User, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(User, on_delete = models.RESTRICT)