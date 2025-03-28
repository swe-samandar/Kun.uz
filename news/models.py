from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=300)
    short_desc = models.CharField(max_length=300)
    description = RichTextField()
    created_at = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return f"{self.title} ({self.category.name})"
    

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    sended_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sended_at', 'is_read']
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        return f"{self.message[:31]} from {self.name}"