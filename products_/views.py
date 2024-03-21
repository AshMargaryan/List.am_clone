from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import ProductSerializer
from .models import Product
from .permissions import IsAuthorOrReadOnly


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author__username', 'category', 'subcategory']


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]


class PostProductView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryProduct(ListAPIView):
    def get_queryset(self):
        self.category = self.kwargs['cat']
        queryset = Product.objects.filter(category=self.category)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = ProductSerializer(queryset, many=True)
        return Response(serializer_class.data)

class SubCategoryProduct(ListAPIView):
    def get_queryset(self):
        self.category = self.kwargs['cat']
        self.subcategory = self.kwargs['subcat']
        queryset = Product.objects.filter(category=self.category, subcategory=self.subcategory)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = ProductSerializer(queryset, many=True)
        return Response(serializer_class.data)



