from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Expense, Category


# Create your views here.

@login_required(login_url='/authentication/login/')
def index (request):

    return render(request,'expenses/index.html',{})


@login_required(login_url='/authentication/login/')
def add_expense (request):

    categories = Category.objects.all()
    context = {
        'categories':categories,
        'values' : request.POST
    }

    if request.method =='POST' :
        amount = request.POST['amount']
        description = request.POST['description']
        category = request.POST['category']
        date = request.POST['date']

        if not amount :
            messages.error(request, 'Amount Required')
            return render(request,'expenses/add_expense.html',context)
        
        if not description :
            messages.error(request, 'Description Required')
            return render(request,'expenses/add_expense.html',context)
        
        if not category :
            messages.error(request, 'Category Required')
            return render(request,'expenses/add_expense.html',context)
        
        if not date :
            messages.error(request, 'Expense date Required')
            return render(request,'expenses/add_expense.html',context)
        
        Expense.objects.create(
            amount = amount,
            description = description,
            category = category,
            date = date,
            owner = request.user,
        )

        messages.success(request, 'Expense Saved')
        return render(request,'expenses/index.html',context)

    
    return render(request,'expenses/add_expense.html',context)

    