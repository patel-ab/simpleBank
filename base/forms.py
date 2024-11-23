from django.forms import ModelForm
from .models import account,customer,transaction



class customerForm(ModelForm):
    class Meta:
        model = customer
        fields = "__all__" 