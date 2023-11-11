from django.urls import path

from apps.users.views import UserSelfProfileView

urlpatterns = [
    path("self/", UserSelfProfileView.as_view(), name="user_profile_detail"),
]
