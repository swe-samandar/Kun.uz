from django.db import models
from django.contrib.auth.models import User
from news.models import News


class UserImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} ning rasmi'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_comments", blank=True)
    views = models.PositiveBigIntegerField(default=0)
    updated_at = models.DateTimeField(blank=True, null=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.content} from {self.user.first_name}"