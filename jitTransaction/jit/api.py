from jit.models import Jit,Transaction
from rest_framework import viewsets,permissions,serializers
from .serializers import JitSerializer,TransactionSerializer



class JitViewSet(viewsets.ModelViewSet):
    queryset = Jit.objects.all()
    permission_classes =[
        permissions.AllowAny
    ]
    serializer_class = JitSerializer

class JitTransaction(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class= TransactionSerializer

