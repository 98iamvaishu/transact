

# Register your models here.
from django.contrib import admin
from transact.models import Lender,Borrower,Paid
# Register your models here.
admin.site.register(Lender)
admin.site.register(Borrower)
admin.site.register(Paid)