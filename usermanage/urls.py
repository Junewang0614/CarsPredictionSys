from django.urls import path
from . import views


urlpatterns = [
    path('reg/',views.register_view),
    path('logon/',views.logon_view),
    path('succ/',views.success_rest_view),
]