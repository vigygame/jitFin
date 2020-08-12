from rest_framework import serializers
from  jit.models import Jit,Transaction,TransactionFile,FailedTransaction



class JitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jit
        fields ='__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields= '__all__'

class FailedTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailedTransaction
        fields= '__all__'


class TransactionFileSerializer(serializers.ModelSerializer):
  	class Meta():
         model = TransactionFile
         fields = '__all__'#('file', 'description', 'uploaded_at')