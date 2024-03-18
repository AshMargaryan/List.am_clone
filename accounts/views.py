from rest_framework.generics import DestroyAPIView
from django.contrib.auth import get_user_model

from .permissions import IsAuthor
from .serializers import UserSerializer


class DeleteAccountView(DestroyAPIView):
    permission_classes = (IsAuthor,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
