from django.shortcuts import render
import csv

# Create your views here.

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from jit.serializers import TransactionFileSerializer,TransactionSerializer

class MyFileView(APIView):
		# MultiPartParser AND FormParser
		# https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
		# "You will typically want to use both FormParser and MultiPartParser
		# together in order to fully support HTML form data."
		parser_classes = (MultiPartParser, FormParser)
		def post(self, request, *args, **kwargs):
				# file_serializer = TransactionFileSerializer(data=request.data)
				# trans=TransactionSerializer(data={"transactionDate" :"2019-07-29","description" :"fuel","category" :2,"amount" :99.888})
				
				file = request.FILES['file'] 
				decoded_file = file.read().decode('utf-8').splitlines()
				reader = csv.DictReader(decoded_file)
				for row in reader:
					print(row)
				
				if trans.is_valid():
    					trans.save()
				if file_serializer.is_valid():
						file_serializer.save()
						return Response(file_serializer.data["file"], status=status.HTTP_201_CREATED)
				else:
						return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)