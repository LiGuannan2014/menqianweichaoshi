from oscar.apps import catalogue, address
from rest_framework import serializers

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = address.models.Country
        fields = (
                'display_order',
                'iso_3166_1_a2',
                'iso_3166_1_a3',
                'iso_3166_1_numeric',
                'name',
                'printable_name',
                'is_shipping_country',
                )

class UserAddressSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(many=False, view_name='user-detail')
    country = serializers.HyperlinkedRelatedField(many=False, view_name='country-detail')

    class Meta:
        model = address.models.UserAddress
        fields = (
                'date_created',
                'hash',
                'is_default_for_billing',
                'is_default_for_shipping',
                'num_orders',
                'phone_number',
                'notes',
                'title',
                'first_name',
                'last_name',
                'line1',
                'line2',
                'line3',
                'line4',
                'state',
                'postcode',
                # 'country',
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
