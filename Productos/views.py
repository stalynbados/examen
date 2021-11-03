from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from Productos.serializers import ProductosSerializer
from Productos.models import Productos

class ListProductosAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class CreateProductosAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class UpdateProductosAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class DeleteProductosAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
