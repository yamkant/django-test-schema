from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    ModelSerializer,
)
from apps.users.models import UserProfile

User = get_user_model()

class UserBaseSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "is_staff",
        ]

class UserSelfProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "gender",
            "date_of_birth",
        ]

    def to_representation(self, instance):
        user_base = UserBaseSerializer(instance.user).data
        profile = super().to_representation(instance)

        representation = {
            "user": user_base,
            "profile": profile,
        }
        return representation
