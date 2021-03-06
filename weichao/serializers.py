from oscar.apps.catalogue import models
from rest_framework import serializers
from django.contrib.auth import User


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail')

    class Meta:
        model = models.Category
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
        model = models.Product
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
        model = models.ProductClass
        fields = (
                'url',
                'name',
                'slug',
                'track_stock',
                'requires_shipping',
                )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
                'last_login',
                'date_joined',
                )
