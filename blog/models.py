from django.db import models


class CreatedDate(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Post(CreatedDate):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_img')

    google = models.URLField(null=True, blank=True)
    microsoft = models.URLField(null=True, blank=True)
    apple = models.URLField(null=True, blank=True)
    amazon = models.URLField(null=True, blank=True)
    netflix = models.URLField(null=True, blank=True)
    spotify = models.URLField(null=True, blank=True)

class Discount(CreatedDate):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='discount_img')
    percentage1 = models.FloatField()
    percentage2 = models.FloatField()
    product_name = models.CharField(max_length=100)

class Resume(CreatedDate):
    title = models.CharField(max_length=50)
    description = models.TextField()
    place= models.TextField()


class Awards(CreatedDate):
    title = models.CharField(max_length=50)
    description = models.TextField()



class About(CreatedDate):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='about_img')


class Comment(CreatedDate):
    description = models.TextField()
    image = models.ImageField(upload_to='comment_img')


class My_services(CreatedDate):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='my_services_img')