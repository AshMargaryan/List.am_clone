from django.urls import path

from .views import DeleteAccountView


urlpatterns = [
    path('<int:pk>', DeleteAccountView.as_view(),),
]