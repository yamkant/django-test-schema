import pytest
from django.urls import reverse_lazy
from rest_framework import status
from django.test import TestCase

@pytest.mark.django_db
class ProductTestCase(TestCase):
    path = reverse_lazy("products:list")
    def test_상품리스트를_조회한다(self):
        response = self.client.get(path=self.path, content_type='application/json')
        assert response.status_code == status.HTTP_200_OK