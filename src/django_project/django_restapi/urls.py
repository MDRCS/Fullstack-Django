from django.conf.urls import url, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloVIEWSET, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet) # you don't need to set basename because it's a Model and  django will figure it out
router.register('login', views.LoginViewSet, basename='login')

urlpatterns = [
    url(r'^hello-view/', views.HelloAPIVIEW.as_view()),
    url(r'', include(router.urls))
]
