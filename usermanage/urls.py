from django.urls import path
from . import views


urlpatterns = [
    path('reg/',views.register_view),
    path('logon/',views.logon_view),
]