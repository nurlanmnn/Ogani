from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Category(AbstractModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = ("Category")
    
    def get_absolute_url(self):
        return reverse('categorie', args=[self.name])
        # return reverse('categorie', arg=self.name)


class Blog(AbstractModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/%Y/%m/%d/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_image = models.ImageField(upload_to='author/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="uncategorized")
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog_details', kwargs={'slug': self.slug})


class News(AbstractModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='news/%Y/%m/%d/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = ("News")
    




