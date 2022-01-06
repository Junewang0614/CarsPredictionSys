from django.urls import path
from . import views,utils


urlpatterns = [
    path('reg/',views.register_view),
    path('logon/',views.logon_view),
    path('succ/',views.success_rest_view),
    path('importfacs/',utils.importfacs),
    path('add_file/',views.add_file_view),
]