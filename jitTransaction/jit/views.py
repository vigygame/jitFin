from django.shortcuts import render
import csv
import json

# Create your views here.

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from jit.serializers import TransactionFileSerializer,TransactionSerializer,FailedTransactionSerializer

class MyFileView(APIView):
		parser_classes = (MultiPartParser, FormParser)
		def post(self, request, *args, **kwargs):
				file_serializer = TransactionFileSerializer(data=request.data)
				file = request.FILES['file'] 
				decoded_file = file.read().decode('utf-8').splitlines()
				reader = csv.DictReader(decoded_file)
				for row in reader:
						print(row["transactionID"])
						trans=TransactionSerializer(data= row)
						if trans.is_valid():
    							trans.save()
						else:
							transactionException = FailedTransactionSerializer(data={"details":json.dumps(row)})
							if transactionException.is_valid():
    								transactionException.save()
							else:
						            print(row)
    					        
				if file_serializer.is_valid():
						file_serializer.save()
						return Response(file_serializer.data, status=status.HTTP_201_CREATED)
				else:
					return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)