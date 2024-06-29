from django.db import models

class TodoItem(models.Model):
    title=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,blank=True)
    

    def __str__(self):
        return self.title

    
