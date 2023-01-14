from django.db import models

# Create your models here.

class AttributeName(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nazev = models.CharField(max_length=15)
    kod = models.CharField(max_length=15, default="", blank=True)
    zobrazit = models.BooleanField(blank=True)

class AttributeValue(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    hodnota = models.CharField(max_length=15)

class Attribute(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nazev_atributu_id = models.ForeignKey(AttributeName, 
            on_delete=models.SET_NULL, null=True)
    hodnota_atributu_id = models.ForeignKey(AttributeValue, 
            on_delete=models.SET_NULL, null=True)

class Product(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nazev = models.CharField(max_length=63, blank=True)
    description = models.CharField(max_length=255, blank=True)
    cena = models.DecimalField(decimal_places=2, max_digits=12)
    mena = models.CharField(max_length=3, blank=True)
    published_on = models.DateTimeField(blank=True)
    is_published = models.BooleanField(blank=True)

class ProductAttributes(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

class Image(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nazev = models.CharField(max_length=63, blank=True)
    obrazek = models.URLField()

class ProductImage(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    obrazek_id = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    nazev = models.CharField(max_length=63)

class Catalog(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nazev = models.CharField(max_length=63)
    obrazek_id = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    products_ids = []
    attributes_ids = []

myModels = {
    "AttributeName": AttributeName,
    "AttributeValue": AttributeValue,
    "Attribute": Attribute,
    "Product": Product,
    "ProductAttributes": ProductAttributes,
    "Image": Image,
    "ProductImage": ProductImage,
    "Catalog": Catalog
    }
