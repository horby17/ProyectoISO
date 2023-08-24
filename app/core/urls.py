from django.urls import path
from core.views import firstview

urlpatterns=[
    path('uno/', firstview),
    path('dos/', firstview)
]