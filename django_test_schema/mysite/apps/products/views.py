from rest_framework.generics import (
    ListAPIView
)

from apps.products.models import Product
from apps.products.serializers import ProductListSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
