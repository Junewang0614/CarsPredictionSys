from django.urls import path
from . import views,utils


urlpatterns = [
    path('reg/',views.register_view),
    path('logon/',views.logon_view),
    path('succ/',views.success_rest_view),
    # path('utils/',utils.importfacs),
]