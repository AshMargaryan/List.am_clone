from django.urls import path

from .views import (ProductListView,
                    ProductDetailView,
                    PostProductView,
                    CategoryProduct,
                    SubCategoryProduct,
                    CreateCategory,
                    CreateSubCategory
                    )

urlpatterns = [
    path('', ProductListView.as_view(),),
    path("<int:pk>/", ProductDetailView.as_view(),),
    path("post-product/", PostProductView.as_view(),),
    path("create-category/", CreateCategory.as_view(),),
    path("create-subcategory/", CreateSubCategory.as_view(),),
    path("category-<str:cat>/", CategoryProduct.as_view(),),
    path("category-<str:cat>/subcategory-<str:subcat>/", SubCategoryProduct.as_view(),),
]