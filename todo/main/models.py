from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)



    
