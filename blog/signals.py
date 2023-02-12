from django.db.models.signals import pre_save
from django.dispatch import receiver
from blog.models import Blog

@receiver(pre_save, sender=Blog)
def blog_pre_save(sender, instance, **kwargs):
    from datetime import datetime
    from django.utils.text import slugify
    instance.slug = slugify(instance.title + '-' + datetime.now().strftime("%Y-%m-%d"))