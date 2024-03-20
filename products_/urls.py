from django.urls import path

from .views import ProductListView, ProductDetailView, PostProductView, CategoryProduct, SubCategoryProduct
from .categories_dict import categories_subcategories

urlpatterns = [
    path('', ProductListView.as_view(),),
    path("<int:pk>/", ProductDetailView.as_view(),),
    path("post_product/", PostProductView.as_view(),),
    path("category_<str:cat>/", CategoryProduct.as_view(),),
    path("category_<str:cat>/subcategory_<str:subcat>/", SubCategoryProduct.as_view(),),
]