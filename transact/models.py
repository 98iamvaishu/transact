

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Lender(models.Model):
    name = models.CharField(max_length=30, null=True)
    initial_amount = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}"


class Borrower(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    amount = models.IntegerField(blank=True, null=True)
    interest = models.FloatField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    terms = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    lender = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    intamt = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.lender}"

class Payments(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    principal_amt = models.FloatField(default=0.0)
    interest_amt = models.FloatField(default=0.0)
    timestamp = models.DateField()

    def __str__(self):
        return f"{self.borrower} | {self.timestamp}"