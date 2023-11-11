import pytest
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
class TestProductListAPI:
    path = reverse_lazy("products:list")

    def test_상품리스트를_조회한다(self):
        client = APIClient()
        response = client.get(self.path)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3