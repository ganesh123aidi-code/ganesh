from django.db import models

# Create your models here
class Category(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  
      
STATUS_CHOICES = (
    ('draft', 'Draft'),    
    ('published', 'Published'),
)   
class Blog(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    short_description = models.CharField(max_length=255)
    blog_body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=0)
    featured_post = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title   