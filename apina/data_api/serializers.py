from rest_framework import serializers

from .models import my_models

class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models["AttributeName"]
        fields = '__all__'

    # Override id field and initialize it without it's default validator.
    # We do this because otherwise serializer does not validate 2nd occurence 
    # of a specific id. In all models.
    id = serializers.IntegerField(validators=[])

    # maybe just
    # "AttributeName": instance
    def to_representation(self, instance):
        #print('instance', instance)
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

    id = serializers.IntegerField(validators=[])

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

    id = serializers.IntegerField(validators=[])

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
        model = my_models["Product"]
        fields = '__all__'

    id = serializers.IntegerField(validators=[])

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

    id = serializers.IntegerField(validators=[])

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

    id = serializers.IntegerField(validators=[])

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

    id = serializers.IntegerField(validators=[])

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

    id = serializers.IntegerField(validators=[])
    #products_ids = serializers.SerializerMethodField()
    #attributes_ids = serializers.SerializerMethodField()

    #def get_products_ids(self, catalog):
     #   return ProductSerializer(catalog.products_ids(), many=True).data

    #def get_attributes_ids(self, catalog):
     #   return AttributeSerializer(catalog.attributes_ids(), many=True).data

    def update(self, item, validated_data):
        """
        Update products_ids and attributes_ids manually.
        Delete the 2 fields from the item so they dont interfere anywhere
        (probably unnecessary).
        """
        if 'nazev' in validated_data.keys():
            item.nazev = validated_data['nazev']
        if 'obrazek_id' in validated_data.keys():
            item.obrazek_id = validated_data['obrazek_id']

        if 'products_ids' in validated_data.keys():
            item.products_ids.clear()
            item.products_ids.set(validated_data['products_ids'])
            # delete it so it doesn't interfere with anything 
            del validated_data['products_ids']

        if 'attributes_ids' in validated_data.keys():
            item.attributes_ids.clear()
            item.attributes_ids.set(validated_data['products_ids'])
            # delete it so it doesn't interfere with anything
            del validated_data['attributes_ids']
        
        return item

    def to_representation(self, instance):
        p_ids = []
        a_ids = []
        for p_id in instance.products_ids.all():
            p_ids.append(p_id.id)
        for a_id in instance.attributes_ids.all():
            a_ids.append(a_id.id)

        return {
                "Catalog": {
                    "id": instance.id,
                    "nazev": instance.nazev,
                    "obrazek_id": instance.obrazek_id_id,
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
