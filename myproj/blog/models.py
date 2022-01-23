from django.db import models
from django.forms import CharField, Textarea
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    discription = models.TextField()
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    photo = models.ImageField()
    file = models.FileField()
    view_count = models.PositiveIntegerField(default=0)
    delete_flag = models.CharField(max_length=1, default="N")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('catube:video_detail', args=[self.pk])


class Comment(models.Model):
    video = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
