from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    author = ,models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_post')
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')