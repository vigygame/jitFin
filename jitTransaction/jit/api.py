from jit.models import Jit,Transaction,TransactionFile
from rest_framework import viewsets,permissions,serializers
from jit.serializers import JitSerializer,TransactionSerializer,TransactionFileSerializer



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

class TransactionFile(viewsets.ModelViewSet):
    queryset = TransactionFile.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class= TransactionFileSerializer

