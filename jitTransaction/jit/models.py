from django.db import models


# Create your models here.
class Jit(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

#  CSV file consists of: 
# i. Transaction Date - YYYY-MM-DD 
# ii. Description - string min 5 chars and max 75 chars 
# iii. Category 
# iv. Amount 
class Transaction(models.Model):
    transactionID =models.CharField(max_length=75)
    transactionDate = models.DateField()
    description = models.CharField(max_length=75)
    category = models.IntegerField()
    amount = models.FloatField()
    FinStatus = models.CharField(max_length=45)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class FailedTransaction(models.Model):
    details=models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

# class FileUpload(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     datafile = models.FileField()

class TransactionFile(models.Model):
    file = models.FileField(blank=False, null=False)
    description = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)