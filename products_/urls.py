from django.urls import path

from .views import ProductListView, ProductDetailView, PostProductView


urlpatterns = [
    path('', ProductListView.as_view(),),
    path("<int:pk>/", ProductDetailView.as_view(),),
    path("post_product", PostProductView.as_view(),),
]