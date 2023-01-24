from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Blog(AbstractModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title