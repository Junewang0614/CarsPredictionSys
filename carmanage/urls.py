from django.urls import path, include
from . import views
from . import utils
urlpatterns = [
    path("",views.test_view),
    path("importcars/",utils.importcars),
    path("importsales/",utils.importsales),
    path("importimage/<str:factory>",utils.importcimages),
]