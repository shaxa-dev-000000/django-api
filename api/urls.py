from django.urls import path
from .views import get_passport

urlpatterns = [
    path("api/passport/<str:passport_id>/", get_passport, name="get_passport"),
]
