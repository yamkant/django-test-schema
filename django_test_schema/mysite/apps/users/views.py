from django.contrib.auth import get_user_model
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.generics import (
    RetrieveAPIView,
)

from .models import UserProfile
from .serializers import UserSelfProfileSerializer

User = get_user_model()

class UserSelfProfileView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSelfProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'