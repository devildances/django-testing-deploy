from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        '''
        this function is used once the user published their post by clicking publish button
        then the system will automatically get the current timezone from the system
        '''
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(appv_comm=True)

    def get_absolute_url(self):
        return reverse('blog:postdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    appv_comm = models.BooleanField(default=False)

    def approve(self):
        self.appv_comm = True
        self.save()

    def get_absolute_url(self):
        return reverse('blog:postlist')

    def __str__(self):
        return self.text