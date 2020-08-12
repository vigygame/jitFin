from rest_framework import routers
from jit.api import JitViewSet,JitTransaction,TransactionFile,JitFailedTransaction
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from jit import views
from jit.views import MyFileView
from django.urls import path, include



router = routers.DefaultRouter()
router.register('api/jit',JitViewSet,'app')
router.register('api/trans',JitTransaction,'JitTransaction')
router.register('api/files',TransactionFile,'fileupload')
router.register('api/filedupload',JitFailedTransaction,'filedupload')



#urlpatterns = router.urls

urlpatterns = [  
  	url(r'^upload/$', MyFileView.as_view(), name='file-upload'),
    path('', include(router.urls))
]

# from django.conf.urls import url
# from jit.views import MyFileView

# urlpatterns = [
#   	url(r'^upload/$', MyFileView.as_view(), name='file-upload'),
# ]