from django.db import models


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=222)
    image = models.ImageField(upload_to="blogs/")
    description = models.TextField()
    description2 = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField(Tag, )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    full_name = models.CharField(max_length=222)
    email = models.EmailField()
    phone = models.CharField(max_length=222)
    messasge = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.full_name


class About(models.Model):
    objects = None
    title = models.CharField(max_length=222)
    image = models.ImageField(upload_to='about/')
    full_name = models.CharField(max_length=222)
    body = models.CharField(max_length=222)
    descriptions = models.TextField()
    insta_link = models.CharField(max_length=222)
    twit_link = models.CharField(max_length=222)
    fase_link = models.CharField(max_length=222)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    full_name = models.CharField(max_length=222)
    email = models.EmailField()
    phone = models.CharField(max_length=222)
    message = models.TextField()

    is_published = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}"


class Subsription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Home(models.Model):
    title = models.TextField()
    name = models.CharField(max_length=222)
    lavozim = models.CharField(max_length=222)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
       return self.name
