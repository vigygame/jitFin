from jit.models import Jit,Transaction,TransactionFile,FailedTransaction,Cards
from rest_framework import viewsets,permissions,serializers
from jit.serializers import JitSerializer,TransactionSerializer,TransactionFileSerializer,FailedTransactionSerializer,CardsSerializer



class JitViewSet(viewsets.ModelViewSet):
    queryset = Jit.objects.all()
    permission_classes =[
        permissions.AllowAny
    ]
    serializer_class = JitSerializer

class CardsViewSet(viewsets.ModelViewSet):
    queryset = Cards.objects.all()
    permission_classes =[
        permissions.AllowAny
    ]
    serializer_class = CardsSerializer

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

class JitFailedTransaction(viewsets.ModelViewSet):
    queryset = FailedTransaction.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class= FailedTransactionSerializer

