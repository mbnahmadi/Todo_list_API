from django.db import models
from authenticate.models import User
# Create your models here.


class TodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Todo List'

    def __str__(self):
        return f'{self.pk}-{self.user.email}'
