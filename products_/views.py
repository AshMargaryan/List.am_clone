from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer
from .models import Product, Category, SubCategory
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
        self.category_name = self.kwargs['cat']
        queryset = Category.objects.filter(name=self.category_name)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = CategorySerializer(queryset, many=True)
        return Response(serializer_class.data)

class SubCategoryProduct(ListAPIView):
    def get_queryset(self):
        self.subcategory_name = self.kwargs['subcat']
        queryset = SubCategory.objects.filter(name=self.subcategory_name)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = SubCategorySerializer(queryset, many=True)
        return Response(serializer_class.data)


class CreateCategory(CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CreateSubCategory(CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


