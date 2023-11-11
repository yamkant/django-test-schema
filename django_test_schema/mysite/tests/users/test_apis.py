import pytest
from django.apps import apps
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase

User = get_user_model()
UserProfile = apps.get_model("users", "UserProfile")
from django.contrib.auth.hashers import make_password


# Normal Test
@pytest.mark.django_db
class TestUserLoginAPI:
    user_credentials = {
        "username": "yamkim",
        "password": "test123!",
    }

    invalid_user_credentials = {
        "username": "something",
        "password": "wrong",
    }

    def test_유저로그인을_확인합니다(self):
        client = APIClient()
        url = resolve_url("auth_login")
        response = client.post(url, self.user_credentials)

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data

        assert "user" in response.data
        assert response.data["user"]["username"] == "yamkim"
        assert response.data["user"]["email"] == "yamkim@example.com"
        assert response.data["user"]["is_staff"] is True