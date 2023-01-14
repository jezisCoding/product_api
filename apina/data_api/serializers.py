from rest_framework import serializers

from .models import myModels

class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModels["AttributeName"]
        fields = '__all__'

    def to_representation(self, instance):
        print("instance:")
        print(type(instance))
        print(dir(instance))
        return {
                "AttributeName": {
                    "id": instance.id,
                    "nazev": instance.nazev,
                    "kod": instance.kod,
                    "zobrazit": instance.zobrazit
                    }
                }

class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModels["AttributeValue"]
        fields = '__all__'

    def to_representation(self, instance):
        return {
                "AttributeValue": {
                    "id": instance.id,
                    "hodnota": instance.hodnota
                    }
                }

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModels["Attribute"]
        fields = '__all__'

    def to_representation(self, instance):
        print("instance:")
        print(type(instance))
        print(instance)
        print(dir(instance))
        print(instance.serializable_value)
        return {
                "Attribute": {
                    "id": instance.id,
                    "nazev_atributu_id": instance.nazev_atributu_id_id,
                    "hodnota_atributu_id": instance.hodnota_atributu_id_id
                    }
                }

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModels["Product"]
        fields = '__all__'

    def to_representation(self, instance):
        return {
                "Product": {
                    "id": instance.id,
                    "nazev": instance.nazev,
                    "description": instance.description,
                    "cena": instance.cena,
                    "mena": instance.mena,
                    "published_on": instance.published_on,
                    "is_published": instance.is_published
                    }
                }

class ProductAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModels["ProductAttributes"]
        fields = '__all__'

    def to_representation(self, instance):
        return {
                "ProductAttributes": {
                    "id": instance.id,
                    "attribute": instance.attribute,
                    "product": instance.product_id
                    }
                }

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModels["Image"]
        fields = '__all__'

    def to_representation(self, instance):
        return {
                "Image": {
                    "id": instance.id,
                    "nazev": instance.nazev,
                    "obrazek": instance.obrazek
                    }
                }

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModels["ProductImage"]
        fields = '__all__'

    def to_representation(self, instance):
        return {
                "ProductImage": {
                    "id": instance.id,
                    "product": instance.product,
                    "obrazekid": instance.obrazekid,
                    "nazev": instance.nazev
                    }
                }

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = myModels["Catalog"]
        fields = '__all__'

    def to_representation(self, instance):
        return {
                "Catalog": {
                    "id": instance.id,
                    "nazev": instance.nazev,
                    "obrazekid": instance.obrazekid,
                    "productids": instance.productids,
                    "attributesids": instance.zevattributesids
                    }
                }

mySerializers = {
        "AttributeName": AttributeNameSerializer,
        "AttributeValue": AttributeValueSerializer,
        "Attribute": AttributeSerializer,
        "Product": ProductSerializer,
        "ProductAttributes": ProductAttributesSerializer,
        "Image": ImageSerializer,
        "ProductImage": ProductImageSerializer,
        "Catalog": CatalogSerializer,
}
