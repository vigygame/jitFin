from rest_framework import serializers
from  jit.models import Jit,Transaction

class JitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jit
        fields ='__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields= '__all__'