from rest_framework import routers
from django.urls import re_path as url , include
from api.views import MoviesList , Register , Collection

router = routers.DefaultRouter()

router.register(r'movies_list', MoviesList, basename='movies_list')
router.register(r'register', Register, basename='register')
router.register(r'collection', Collection, basename='collection')


urlpatterns = [
        url(r'^', include(router.urls)),
]