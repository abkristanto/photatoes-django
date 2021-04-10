from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name
    def query_set(self):
        return Category.objects.all()

class Image(models.Model):
    imageName = models.CharField(max_length=150)
    imageAperture = models.DecimalField(max_digits=3, decimal_places=2)
    imageShutterSpeed = models.IntegerField()
    imageISO = models.IntegerField()
    imageCamera = models.CharField(max_length=150)
    imageFile = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.imageName

class Photographer(models.Model):
    photographerName = models.CharField(max_length=100)
    photographerProfileDesc = models.TextField()
    photographerProfilePic = models.ImageField(upload_to='pics')
    photographerTwitter = models.URLField()
    photographerLinkedIn = models.URLField()

    def __str__(self):
        return self.photographerName

class Portfolio(models.Model):
    portfolioName = models.CharField(max_length=100)
    portfolioClient = models.CharField(max_length=150)
    portfolioCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    portfolioImageOne = models.ForeignKey(Image, null=True, related_name='photo1', on_delete=models.SET_NULL)
    portfolioImageTwo = models.ForeignKey(Image, null=True, related_name='photo2', on_delete=models.SET_NULL)
    portfolioImageThree = models.ForeignKey(Image, null=True, related_name='photo3', on_delete=models.SET_NULL)
    portfolioPhotographer = models.ForeignKey(Photographer, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.portfolioName

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name

class PhotographerPortfolio(models.Model):
    photographerID = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    portfolioID = models.ForeignKey(Photographer, on_delete=models.CASCADE)




