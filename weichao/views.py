from oscar.apps.catalogue.models import *
from weichao.serializers import *
from rest_framework import generics

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductClassList(generics.ListCreateAPIView):
    queryset = ProductClass.objects.all()
    serializer_class = ProductClassSerializer

class ProductClassDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductClass.objects.all()
    serializer_class = ProductClassSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializers_class = UserSerializer
