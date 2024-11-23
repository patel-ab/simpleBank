from django.db import models

# Create your models here.
class Customer(models.Model):
    custId=models.IntegerField(unique=True,null=True)
    name=models.TextField(max_length=50,null=True)
    password=models.TextField(max_length=50,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.custId:
            last_custId = Customer.objects.all().aggregate(largest=models.Max('custId'))['largest']
            self.custId = 100 if last_custId is None else last_custId + 1
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.name if self.name else "No Name"


class Account(models.Model):
    custId=models.IntegerField(unique=True)
    name=models.TextField(max_length=50,null=True)
    amount=models.IntegerField(null=True)

    def __str__(self):
        return self.name if self.name else "No Name"
    

class Transaction(models.Model):
    custId=models.IntegerField()
    trans_type=models.TextField(max_length=50,null=True)
    trans_amount=models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trans_type if self.trans_type else "No Name"




