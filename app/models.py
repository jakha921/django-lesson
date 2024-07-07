from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # obj = Category.objects.all()
    # print(obj) # Category object (1)
    # print(obj) # 'name', 'foo', 'bar', 'baz'

    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'category'
        ordering = ['name']
        db_table = 'categories'


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'  # chernovik
        PUBLISHED = 'published', 'Published'  # opublikovano

    # id = models.AutoField(primary_key=True, unique=True)  # auto incrementing field optional
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='news/images/')  # create a folder name media in the root directory
    slug = models.SlugField(max_length=100, unique=True)
    publish_time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # uzb, rus, eng
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'posts'
        verbose_name = 'post'
        ordering = ['-publish_time']  # [3, 2, 1]
        db_table = 'posts'
