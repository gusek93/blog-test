from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    #PostSearchView
)

router = DefaultRouter(trailing_slash=False)
router.register('posts', PostViewSet)


urlpatterns = [

]
urlpatterns += router.urls

