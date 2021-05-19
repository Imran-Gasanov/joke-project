from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'jokes', views.JokeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generate/', views.GenerateJokeView.as_view())
]
