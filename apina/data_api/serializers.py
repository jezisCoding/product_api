from rest_framework import serializers

from .models import my_models

class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models["AttributeName"]
        fields = '__all__'

    # Override id field and initialize it without it's default validator (unique).
    # We do this because otherwise serializer does not validate 2nd occurence 
    # of a specific id. In all models.
    #id = serializers.IntegerField(validators=[])

    def to_representation(self, instance):
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
        model = my_models["AttributeValue"]
        fields = '__all__'

    #id = serializers.IntegerField(validators=[])

    def to_representation(self, instance):
        return {
                "AttributeValue": {
                    "id": instance.id,
                    "hodnota": instance.hodnota
                    }
                }


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models["Attribute"]
        fields = '__all__'

    #id = serializers.IntegerField(validators=[])

    def to_representation(self, instance):
        return {
                "Attribute": {
                    "id": instance.id,
                    "nazev_atributu_id": instance.nazev_atributu_id,
                    "hodnota_atributu_id": instance.hodnota_atributu_id
                    }
                }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models["Product"]
        fields = '__all__'

    #id = serializers.IntegerField(validators=[])

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
        model = my_models["ProductAttributes"]
        fields = '__all__'

    #id = serializers.IntegerField(validators=[])

    def to_representation(self, instance):
        return {
                "ProductAttributes": {
                    "id": instance.id,
                    "attribute": instance.attribute_id,
                    "product": instance.product_id
                    }
                }


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models["Image"]
        fields = '__all__'

    #id = serializers.IntegerField(validators=[])

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
        model = my_models["ProductImage"]
        fields = '__all__'

    #id = serializers.IntegerField(validators=[])

    def to_representation(self, instance):
        return {
                "ProductImage": {
                    "id": instance.id,
                    "product": instance.product_id,
                    "obrazek_id": instance.obrazek_id,
                    "nazev": instance.nazev
                    }
                }


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models["Catalog"]
        fields = '__all__'

    #id = serializers.IntegerField(validators=[])

    def update(self, item, validated_data):
        """
        Update products_ids and attributes_ids manually.
        Delete the 2 fields from the item so they dont interfere anywhere.
        """
        if 'nazev' in validated_data.keys():
            item.nazev = validated_data['nazev']
        if 'obrazek_id' in validated_data.keys():
            item.obrazek = validated_data['obrazek_id']

        if 'products_ids' in validated_data.keys():
            item.products.clear()
            item.products.set(validated_data['products_ids'])
            del validated_data['products_ids']

        if 'attributes_ids' in validated_data.keys():
            item.attributes.clear()
            item.attributes.set(validated_data['products_ids'])
            del validated_data['attributes_ids']
        
        #item.save()
        return item

    def to_representation(self, instance):
        p_ids = []
        a_ids = []
        for p_id in instance.products.all():
            p_ids.append(p_id.id)
        for a_id in instance.attributes.all():
            a_ids.append(a_id.id)

        return {
                "Catalog": {
                    "id": instance.id,
                    "nazev": instance.nazev,
                    "obrazek_id": instance.obrazek_id,
                    "products_ids": p_ids,
                    "attributes_ids": a_ids
                    }
                }


my_serializers = {
        "AttributeName": AttributeNameSerializer,
        "AttributeValue": AttributeValueSerializer,
        "Attribute": AttributeSerializer,
        "Product": ProductSerializer,
        "ProductAttributes": ProductAttributesSerializer,
        "Image": ImageSerializer,
        "ProductImage": ProductImageSerializer,
        "Catalog": CatalogSerializer,
}
