from django.db import models
from django.contrib.auth.models import User


def get_current_user():
    return User.objects.get(username='admin')



class Property(models.Model):
    name = models.CharField("Name: ", max_length=255)
    description = models.TextField("Description: ")
    price = models.DecimalField("Price: ", max_digits=10, decimal_places=2)
    address = models.CharField("Address: ", max_length=255)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    squareArea = models.DecimalField(max_digits=8, decimal_places=2)
    repairQuality = models.CharField("Repair Quality", max_length=20)
    photo = models.URLField("URL: ", default="https://i.ytimg.com/vi/n8vcZVHjXeQ/maxresdefault.jpg")
    status = models.BooleanField("Status: ")
    isRent = models.BooleanField("Rent: ", default=True)
    isBuy = models.BooleanField("Buy: ", default=True)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=get_current_user)

    def __str__(self):
        return self.name



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class FAQ(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)


class RentHistory(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.username


class SalesHistory(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    dateOfSale = models.DateField()
    priceOfSale = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.username
