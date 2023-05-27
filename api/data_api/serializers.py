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


class AttributeSerializer(serializers.Serializer):
    """
    We don't use ModelSerializer because the JSON fields don't match the Models.
    """
    id = serializers.IntegerField(validators=[])
    nazev_atributu_id = serializers.IntegerField()
    hodnota_atributu_id = serializers.IntegerField()

    # It might be appropriate to use validators in creates() and updates()
    def create(self, validated_data):
        return my_models['Attribute'].objects.create(
            id = validated_data.get('id'), 
            nazev_atributu = my_models['AttributeName'].objects.get(
                pk=validated_data.get('nazev_atributu_id')),
            hodnota_atributu = my_models['AttributeValue'].objects.get(
                pk=validated_data.get('hodnota_atributu_id')))

    def update(self, instance, validated_data):
        instance.nazev_atributu = my_models['AttributeName'].objects.get(
            pk=validated_data.get('nazev_atributu_id'))
        instance.hodnota_atributu = my_models['AttributeValue'].objects.get(
            pk=validated_data.get('hodnota_atributu_id'))
        instance.save()
        return instance

    def to_representation(self, instance):
        return {
                "Attribute": {
                    "id": instance.id,
                    "nazev_atributu_id": instance.nazev_atributu_id,
                    "hodnota_atributu_id": instance.hodnota_atributu_id
                    }
                }


class ProductSerializer(serializers.Serializer):
    """
    We don't use ModelSerializer because of the validators in this case?
    """
    id = serializers.IntegerField(validators=[])
    nazev = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    cena = serializers.FloatField(required=False)
    mena = serializers.CharField(required=False)
    published_on = serializers.DateTimeField(required=False, allow_null=True)
    is_published = serializers.BooleanField(required=False)

    def create(self, validated_data):
        kwparams = {}
        if 'id' in validated_data.keys():
            id = validated_data.get('id')
            kwparams['id'] = id 
        if 'nazev' in validated_data.keys():
            nazev = validated_data.get('nazev')
            kwparams['nazev'] = nazev
        if 'description' in validated_data.keys():
            description = validated_data.get('description')
            kwparams['description'] = description
        if 'cena' in validated_data.keys():
            cena = validated_data.get('cena')
            kwparams['cena'] = cena
        if 'mena' in validated_data.keys():
            mena = validated_data.get('mena')
            kwparams['mena'] = mena
        if 'published_on' in validated_data.keys():
            published_on = validated_data.get('published_on')
            kwparams['published_on'] = published_on
        if 'is_published' in validated_data.keys():
            is_published = validated_data.get('is_published')
            kwparams['is_published'] = is_published
        print(kwparams)
        return my_models['Product'].objects.create(**kwparams)

    def update(self, instance, validated_data):
        if 'nazev' in validated_data.keys():
            instance.nazev = validated_data.get('nazev')
        if 'description' in validated_data.keys():
            instance.description = validated_data.get('description')
        if 'cena' in validated_data.keys():
            instance.cena = validated_data.get('cena')
        if 'mena' in validated_data.keys():
            instance.mena = validated_data.get('mena')
        if 'published_on' in validated_data.keys():
            instance.published_on = validated_data.get('published_on')
        if 'is_published' in validated_data.keys():
            instance.is_published = validated_data.get('is_published')
        instance.save()
        return instance

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


class ProductImageSerializer(serializers.Serializer):
    """
    We don't use ModelSerializer because the JSON fields don't match the Models.
    """
    id = serializers.IntegerField(validators=[])
    product = serializers.IntegerField()
    obrazek_id = serializers.IntegerField()
    nazev = serializers.CharField()

    def create(self, validated_data):
        return my_models['ProductImage'].objects.create(
            id = validated_data['id'],
            product = my_models['Product'].objects.get(
                pk=validated_data['product']),
            obrazek = my_models['Image'].objects.get(
                pk=validated_data['obrazek_id']),
            nazev = validated_data['nazev'])

    def update(self, instance, validated_data):
        instance.product = my_models['Product'].objects.get(
            pk=validated_data['product'])
        instance.obrazek = my_models['Image'].objects.get(
            pk=validated_data['obrazek_id'])
        instance.nazev = validated_data['nazev']
        instance.save() 
        return instance

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
    """
    We don't use ModelSerializer because the JSON fields don't match the Models.
    """
    class Meta:
        model = my_models["Image"]
        fields = '__all__'

    #id = serializers.IntegerField(validators=[])

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

#class CatalogSerializer(serializers.Serializer):
#    """
#    We don't use ModelSerializer because the JSON fields don't match the Models.
#    """
#    id = serializers.IntegerField(validators=[])
#
#    def create(self, validated_data):
#        print(validated_data)
#        kwparams = {}
#        # create needs an id
#        #if 'id' in validated_data.keys():
#        #    id = validated_data.get('id')
#        #    kwparams['id'] = id 
#        if 'nazev' in validated_data.keys():
#            kwparams['nazev'] = validated_data.get('nazev')
#        if 'obrazek_id' in validated_data.keys():
#            kwparams['obrazek_id'] = validated_data.get('obrazek_id')
#        print(validated_data['products_ids'])
#        if 'products_ids' in validated_data.keys():
#            kwparams['products_ids'] = validated_data.get('products_ids')
#        if 'attributes_ids' in validated_data.keys():
#            kwparams['attributes_ids'] = validated_data.get('attributes_ids')
#        #kwparams['products_ids'] = my_models['Product'].objects.get(
#        #    pk=validated_data.get('products_ids'))#products_ids spatne
#        #kwparams['attributes_ids'] = my_models['Attribute'].objects.get(
#        #    pk=validated_data.get('attributes_ids'))
#        print(kwparams)
#        print(**kwparams)
#        return my_models['Catalog'].objects.create(**kwparams)
#
#    def update(self, item, validated_data):
#        """
#        Update products_ids and attributes_ids manually.
#        Delete the 2 fields from the item so they dont interfere anywhere.
#        """
#        if 'nazev' in validated_data.keys():
#            item.nazev = validated_data['nazev']
#        if 'obrazek_id' in validated_data.keys():
#            item.obrazek = validated_data['obrazek_id']
#
#        if 'products_ids' in validated_data.keys():
#            item.products.clear()
#            item.products.set(validated_data['products_ids'])
#            del validated_data['products_ids']
#
#        if 'attributes_ids' in validated_data.keys():
#            item.attributes.clear()
#            item.attributes.set(validated_data['products_ids'])
#            del validated_data['attributes_ids']
#        
#        item.save()
#        return item
#
#    def to_representation(self, instance):
#        p_ids = []
#        a_ids = []
#        for p_id in instance.products.all():
#            p_ids.append(p_id.id)
#        for a_id in instance.attributes.all():
#            a_ids.append(a_id.id)
#
#        return {
#                "Catalog": {
#                    "id": instance.id,
#                    "nazev": instance.nazev,
#                    "obrazek_id": instance.obrazek_id,
#                    "products_ids": p_ids,
#                    "attributes_ids": a_ids
#                    }
#                }


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
