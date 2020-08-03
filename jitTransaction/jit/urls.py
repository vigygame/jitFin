from rest_framework import routers
from .api import JitViewSet,JitTransaction
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from jit import views



router = routers.DefaultRouter()
router.register('api/jit',JitViewSet,'app')
router.register('api/trans',JitTransaction,'JitTransaction')
#router.urls.append (views.upload)

urlpatterns = router.urls
