from django.db import models

# Create your models here.

class AttributeName(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nazev = models.CharField(max_length=31, default="", blank=True)
    kod = models.CharField(max_length=31, default="", blank=True)
    zobrazit = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.__class__.__name__, str(self.id), self.nazev)


class AttributeValue(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    hodnota = models.CharField(max_length=31)

    def __str__(self):
        return '{0} {1} {2}'.format(self.__class__.__name__, str(self.id), self.hodnota)


class Attribute(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nazev_atributu_id = models.ForeignKey(AttributeName, 
            on_delete=models.SET_NULL, null=True)
    hodnota_atributu_id = models.ForeignKey(AttributeValue, 
            on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.__class__.__name__, str(self.id))


class Product(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nazev = models.CharField(max_length=63)
    description = models.CharField(max_length=255, blank=True)
    cena = models.DecimalField(decimal_places=2, max_digits=12)
    mena = models.CharField(max_length=3)
    published_on = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.__class__.__name__, str(self.id), self.nazev)


class ProductAttributes(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    attribute_id = models.ForeignKey(Attribute, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.__class__.__name__, str(self.id))


class Image(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nazev = models.CharField(max_length=63, blank=True)
    obrazek = models.URLField()

    def __str__(self):
        return '{0} {1} {2}'.format(self.__class__.__name__, str(self.id), self.nazev)


class ProductImage(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    obrazek_id = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    nazev = models.CharField(max_length=63)

    def __str__(self):
        return '{0} {1} {2}'.format(self.__class__.__name__, str(self.id), self.nazev)


class Catalog(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    nazev = models.CharField(max_length=63, default="", blank=True)
    obrazek_id = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    # These are the list fields
    products_ids = models.ManyToManyField(Product, blank=True)
    attributes_ids = models.ManyToManyField(Attribute, blank=True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.__class__.__name__, str(self.id), self.nazev)


my_models = {
    "AttributeName": AttributeName,
    "AttributeValue": AttributeValue,
    "Attribute": Attribute,
    "Product": Product,
    "ProductAttributes": ProductAttributes,
    "Image": Image,
    "ProductImage": ProductImage,
    "Catalog": Catalog
    }
