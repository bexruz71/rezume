from django.db import models


class CreatedDate(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class Brand(CreatedDate):
    title = models.CharField(max_length=100)
    google = models.URLField(null=True, blank=True)
    microsoft = models.URLField(null=True, blank=True)
    apple = models.URLField(null=True, blank=True)
    amazon = models.URLField(null=True, blank=True)
    netflix = models.URLField(null=True, blank=True)
    spotify = models.URLField(null=True, blank=True)

    def str(self):
        return self.title

class Portfolio(CreatedDate):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio_img')
    names = models.CharField(max_length=100)

    def str(self):
        return self.title



class Discount(CreatedDate):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='discount_img')
    percentage1 = models.FloatField()
    percentage2 = models.FloatField()
    product_name = models.CharField(max_length=100)
    downloads = models.IntegerField()
    rate = models.FloatField()
    recognition = models.FloatField()
    price = models.FloatField()


    def str(self):
        return self.title


class Resume(CreatedDate):
    title = models.CharField(max_length=50)
    description = models.TextField()
    place= models.TextField()

    def str(self):
        return self.title


class Awards(CreatedDate):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def str(self):
        return self.title



class About(CreatedDate):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author_image = models.ImageField(upload_to='about_img')

    def str(self):
        return self.title


class Comment(CreatedDate):
    author_image = models.ImageField(upload_to='comment_img')
    description = models.TextField()
    author_name = models.CharField(max_length=100)

    def str(self):
        return self.author_name


class Service(CreatedDate):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def str(self):
        return self.title



class Blog(CreatedDate):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_img')


    def str(self):
        return self.title

class Contact(CreatedDate):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

    def str(self):
        return self.name









