from rest_framework import serializers

from .models import my_models

class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = my_models["AttributeName"]
        fields = '__all__'

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
    id = serializers.IntegerField(required=True)
    # DOES NOT MATCH SERIALIZER (MATCHES MODEL)
    nazev_atributu_id = serializers.IntegerField()
    # DOES NOT MATCH SERIALIZER (MATCHES MODEL)
    hodnota_atributu_id = serializers.IntegerField()

    # It might be appropriate to use validators in creates() and updates()
    def create(self, validated_data):
        create_params = {}
        if 'id' in validated_data.keys():
            id = validated_data.get('id'),
            create_params['id'] = id
        # Here we dont use _id because in Django it's an actual reference
        # to the object, not just the id. So in the model i didn't use id
        if 'nazev_atributu_id' in validated_data.keys():
            # DOES NOT MATCH SERIALIZER (MATCHES MODEL)
            nazev_atributu = my_models['AttributeName'].objects.get(
                pk=validated_data.get('nazev_atributu_id')),
            create_params['nazev_atributu'] = nazev_atributu
        if 'hodnota_atributu_id' in validated_data.keys():
            # DOES NOT MATCH SERIALIZER (MATCHES MODEL)
            hodnota_atributu = my_models['AttributeValue'].objects.get(
                pk=validated_data.get('hodnota_atributu_id'))
            create_params['hodnota_atributu'] = hodnota_atributu
        return my_models['Attribute'].objects.create(**create_params)

    def update(self, instance, validated_data):
        if 'nazev_atributu_id' in validated_data.keys():
            instance.nazev_atributu = my_models['AttributeName'].objects.get(
                pk=validated_data.get('nazev_atributu_id'))
        if 'hodnota_atributu_id' in validated_data.keys():
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
    id = serializers.IntegerField(required=True)
    nazev = serializers.CharField(required=False, max_length=63)
    description = serializers.CharField(required=False)
    cena = serializers.FloatField(required=False)
    mena = serializers.CharField(required=False)
    published_on = serializers.DateTimeField(required=False, allow_null=True)
    is_published = serializers.BooleanField(required=False)

    def create(self, validated_data):
        create_params = {}
        if 'id' in validated_data.keys():
            id = validated_data.get('id')
            create_params['id'] = id
        if 'nazev' in validated_data.keys():
            nazev = validated_data.get('nazev')
            create_params['nazev'] = nazev
        if 'description' in validated_data.keys():
            description = validated_data.get('description')
            create_params['description'] = description
        if 'cena' in validated_data.keys():
            cena = validated_data.get('cena')
            create_params['cena'] = cena
        if 'mena' in validated_data.keys():
            mena = validated_data.get('mena')
            create_params['mena'] = mena
        if 'published_on' in validated_data.keys():
            published_on = validated_data.get('published_on')
            create_params['published_on'] = published_on
        if 'is_published' in validated_data.keys():
            is_published = validated_data.get('is_published')
            create_params['is_published'] = is_published
        print(create_params)
        return my_models['Product'].objects.create(**create_params)

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
    id = serializers.IntegerField(required=True)
    product = serializers.IntegerField()
    # DOES NOT MATCH SERIALIZER (MATCHES MODEL)
    obrazek_id = serializers.IntegerField()
    nazev = serializers.CharField()

    def create(self, validated_data):
        create_params = {}
        if 'id' in validated_data.keys():
            id = validated_data['id']
            create_params['id'] = id
        if 'product' in validated_data.keys():
            product = my_models['Product'].objects.get(
                pk=validated_data['product'])
            create_params['product'] = product
        if 'obrazek_id' in validated_data.keys():
            # DOES NOT MATCH SERIALIZER (MATCHES MODEL)
            # is it here because we want to run it through serializer validation?
            obrazek = my_models['Image'].objects.get(
                pk=validated_data['obrazek_id'])
            create_params['obrazek'] = obrazek
        if 'nazev' in validated_data.keys():
            nazev = validated_data['nazev']
            create_params['nazev'] = nazev
        return my_models['ProductImage'].objects.create(**create_params)

    def update(self, instance, validated_data):
        if 'product' in validated_data.keys():
            instance.product = my_models['Product'].objects.get(
                pk=validated_data['product'])
        if 'obrazek_id' in validated_data.keys():
            instance.obrazek = my_models['Image'].objects.get(
                pk=validated_data['obrazek_id'])
        if 'nazev' in validated_data.keys():
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
    class Meta:
        model = my_models["Image"]
        fields = '__all__'

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
#    We don't use ModelSerializer because the test data JSON fields don't 
#    match the Models.
#    """
#    id = serializers.IntegerField()
#
#    def create(self, validated_data):
#        print(validated_data)
#        create_params = {}
#        # create needs an id
#        #if 'id' in validated_data.keys():
#        #    id = validated_data.get('id')
#        #    create_params['id'] = id
#        if 'nazev' in validated_data.keys():
#            create_params['nazev'] = validated_data.get('nazev')
#        if 'obrazek_id' in validated_data.keys():
#            create_params['obrazek_id'] = validated_data.get('obrazek_id')
#        print(validated_data['products_ids'])
#        if 'products_ids' in validated_data.keys():
#            create_params['products_ids'] = validated_data.get('products_ids')
#        if 'attributes_ids' in validated_data.keys():
#            create_params['attributes_ids'] = validated_data.get('attributes_ids')
#        #create_params['products_ids'] = my_models['Product'].objects.get(
#        #    pk=validated_data.get('products_ids'))#products_ids spatne
#        #create_params['attributes_ids'] = my_models['Attribute'].objects.get(
#        #    pk=validated_data.get('attributes_ids'))
#        print(create_params)
#        print(**create_params)
#        return my_models['Catalog'].objects.create(**create_params)
#
#    def update(self, instance, validated_data):
#        """
#        Update products_ids and attributes_ids manually.
#        Delete the 2 fields from the instance so they dont interfere anywhere.
#        """
#        if 'nazev' in validated_data.keys():
#            instance.nazev = validated_data['nazev']
#        if 'obrazek_id' in validated_data.keys():
#            instance.obrazek = validated_data['obrazek_id']
#
#        if 'products_ids' in validated_data.keys():
#            instance.products.clear()
#            instance.products.set(validated_data['products_ids'])
#            del validated_data['products_ids']
#
#        if 'attributes_ids' in validated_data.keys():
#            instance.attributes.clear()
#            instance.attributes.set(validated_data['products_ids'])
#            del validated_data['attributes_ids']
#        
#        instance.save()
#        return instance
#
#    def update(self, instance, validated_data):
#        instance.product = my_models['Product'].objects.get(
#            pk=validated_data['product'])
#        instance.obrazek = my_models['Image'].objects.get(
#            pk=validated_data['obrazek_id'])
#        instance.nazev = validated_data['nazev']
#        instance.save()
#        return instance
#
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
