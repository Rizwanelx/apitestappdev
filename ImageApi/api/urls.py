from django.conf.urls import url, include
from rest_framework import routers
from ImageApi.api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]