from django.db import models
from manage import init_django

init_django()


class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Platform(Model):
    title = models.CharField(max_length=255)


class Publisher(Model):
    title = models.CharField(max_length=255)


class ContentRating(Model):
    title = models.CharField(max_length=255)
    ageLimit = models.IntegerField()
    description = models.CharField(max_length=255)


class Genre(Model):
    title = models.CharField(max_length=255)


class Products(Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    platform = models.ForeignKey(
        Platform, on_delete=models.CASCADE
    )
    release_Date = models.DateTimeField()
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE
    )
    price = models.IntegerField()
    contentRating = models.ForeignKey(
        ContentRating, on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE
    )
    isAvailable = models.BooleanField()


class Customer(Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone_Num = models.CharField(max_length=255)
    Date_Of_Both = models.DateTimeField()


class Sales(Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )
    address = models.CharField(max_length=255)
    date_Of_Sales = models.DateTimeField()


class Discount(Model):
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE
    )
    date_From = models.DateTimeField()
    date_Until = models.DateTimeField()
    PRC = models.DecimalField(decimal_places=2, max_digits=2)


class WISH_LIST(Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )


class WL_P(Model):
    product = models.ManyToManyField(Products)
    wish_list = models.ManyToManyField(WISH_LIST)
