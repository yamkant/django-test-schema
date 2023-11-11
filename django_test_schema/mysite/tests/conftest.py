import os

import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command
from rest_framework.test import APIClient
from apps.users.models import UserProfile
from project.settings import BASE_DIR

User = get_user_model()

@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        dir_path = os.path.join(BASE_DIR, f"tests/fixtures")
        files = os.listdir(dir_path)
        for file in files:
            call_command("loaddata", f"tests/fixtures/{file}")
