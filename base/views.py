from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Account, Transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
import re

# Create your views here.


def default(request):
    if request.method == "POST":
        return redirect("Login")

    return render(request, "default.html")

def login(request):
    if request.method == "POST":
        cust_name = request.POST.get("name")
        cust_pwd = request.POST.get("password")
        
        try:
            c_object = Customer.objects.get(name=cust_name)
            a_object = Account.objects.get(name=cust_name)
            
            if c_object.password == cust_pwd:
                request.session['customer_name'] = c_object.name
                request.session['customer_amount'] = a_object.amount
                request.session['customer_id'] = c_object.custId
                return redirect("Home")
            else:
                messages.error(request, "Invalid password.")
        
        except Customer.DoesNotExist:
            messages.error(request, "Customer does not exist.")
        except Account.DoesNotExist:
            messages.error(request, "Account does not exist.")
    
    return render(request, "login.html")


def checkIfCustomerExist(newName):
    check = Account.objects.filter(name=newName).first()

    if check is None:
        return False
    else:
        return True




def signup(request):
    if request.method == "POST":
        cust_name = request.POST.get("name", "").strip()  # Strip whitespace
        cust_pwd = request.POST.get("password", "").strip()  # Strip whitespace

        # Check if name contains any numbers
        if any(char.isdigit() for char in cust_name):
            messages.error(request, "Invalid input: Name should not contain numbers.")
            return render(request, 'signup.html')

        # Check if customer already exists
        if checkIfCustomerExist(cust_name):
            messages.error(request, "Customer already exists.")
            return render(request, 'signup.html')

        # Check if form data is valid (name and password provided)
        if cust_name and cust_pwd:
            # Create Customer and Account
            Customer.objects.create(name=cust_name, password=cust_pwd)
            c_object = Customer.objects.get(name=cust_name)
            cid = c_object.custId
            Account.objects.create(custId=cid, name=cust_name, amount=0)
            messages.success(request, "Account created successfully.")
        else:
            messages.error(request, "Form data is invalid. Please fill out all fields.")

    return render(request, 'signup.html')


def home(request):
    c_id = request.session.get('customer_id')  
    if not c_id:  # Redirect to login if session doesn't exist
        return redirect("Login")

    a_obj = Account.objects.get(custId=c_id)
    c_obj = Customer.objects.get(custId=c_id)
    c_amount = a_obj.amount

    if request.method == "POST":
        # Handle logout
        if request.POST.get("signout"):
            logout(request)  # Clear session and log out
            return redirect("Login")

        # Handle transactions
        transaction_type = request.POST.get("transaction_type")
        amount = request.POST.get("amount")
        customer_id = request.POST.get("customer_id")

        if amount and customer_id and customer_id == str(c_id):
            amount_float = float(amount)
            if transaction_type == "deposit":
                a_obj.amount += amount_float
                Transaction.objects.create(custId=c_id, trans_type="Deposit", trans_amount=amount_float)
            elif transaction_type == "withdraw":
                if a_obj.amount >= amount_float:
                    a_obj.amount -= amount_float
                    Transaction.objects.create(custId=c_id, trans_type="Withdraw", trans_amount=amount_float)
                else:
                    context = {
                        'error': "Insufficient balance!",
                        'customer_name': c_obj.name,
                        'customer_amount': c_amount,
                        'transactions': Transaction.objects.filter(custId=c_id).values_list('trans_type', 'trans_amount')
                    }
                    return render(request, "home.html", context)

            a_obj.save()
            request.session['customer_amount'] = a_obj.amount
            c_amount = a_obj.amount
            return redirect("Home")

    context = {
        'customer_name': c_obj.name,
        'customer_amount': c_amount,
        'customer_id': c_id,
        'transactions': Transaction.objects.filter(custId=c_id).values_list('trans_type', 'trans_amount')
    }
    return render(request, 'home.html', context)

def signout(request):
    if request.method == 'POST':
        logout(request)  # Log out the user
        return redirect('Login')  # Redirect to login page or any other page
    return redirect('Home')  # Redirect to home if accessed via GET or invalid request


def zelle(request):
    c_id = request.session['customer_id']
    c_obj = Customer.objects.get(custId=c_id)


    if request.method == "POST":
        
        transfer_amount = request.POST.get("amount")
        receiver_name = request.POST.get("receiverName")
        a_obj = Account.objects.get(custId=c_id)

        if a_obj.amount < int(transfer_amount):
            messages.error(request, "You Poor")
        
        receiver_a_obj = Account.objects.filter(name=receiver_name).first()

        if receiver_a_obj is None:
                messages.error(request, "Enter details correctly")
        
        else:   
            
           # receiver_a_obj = Account.objects.filter(name=receiver_name).first()
           # if receiver_a_obj is None:
           #     messages.error(request, "You Stupid")
                
            a_obj.amount= a_obj.amount-int(transfer_amount)
            receiver_a_obj.amount = receiver_a_obj.amount + int(transfer_amount)
            Transaction.objects.create(custId=c_id, trans_type="Mondey Sent via Zelle", trans_amount=int(transfer_amount))
            Transaction.objects.create(custId=receiver_a_obj.custId, trans_type="Mondey Received via Zelle", trans_amount=int(transfer_amount))
            a_obj.save()
            receiver_a_obj.save()

            context = {
                'customer_name': c_obj.name,
                'customer_amount': a_obj.amount,
                'customer_id': c_id,
                'transactions': Transaction.objects.filter(custId=c_id).values_list('trans_type', 'trans_amount')
            }
            return redirect("Home")

        



    return render(request, "zelle.html")
