from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .producer import publish
from .serializers import ProductSerializer
from rest_framework import viewsets, status
import random


class ProductViewSet(viewsets.ViewSet):
    # /api/product route, GET request
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # /api/products, POST request
    def create(self, request):
        print("Data ", request.data)
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('create', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # /api/products/<str:id>
    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # /api/products/<str:id>
    def destroyer(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        publish('deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        print("Found users ", len(users))
        if len(users) == 0:
            return Response({"INFO": "no users in db"})
        user = random.choice(users)
        return Response({
            'id': user.id
        })