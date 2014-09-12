from oscar.apps import catalogue, address
from rest_framework import serializers

class UserAddressSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(many=False, view_name='user-detail')

    class Meta:
        model = address.models.UserAddress
        fields = (
                'is_default_for_shipping',
                'is_default_for_billing',
                'num_orders',
                'hash',
                'date_created',
                )

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail')

    class Meta:
        model = catalogue.models.Category
        fields = (
                'name',
                'image',
                'slug',
                'description',
                'full_name',
                )

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    parent = serializers.HyperlinkedRelatedField(many=False, view_name='product-detail')
    recommeded_products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail')

    class Meta:
        model = catalogue.models.Product
        fields = (
                'upc',
                'url',
                'title',
                'slug',
                'description',
                'parent',
                'recommended_products',
                )

class ProductClassSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail')

    class Meta:
        model = catalogue.models.ProductClass
        fields = (
                'url',
                'name',
                'slug',
                'track_stock',
                'requires_shipping',
                )
