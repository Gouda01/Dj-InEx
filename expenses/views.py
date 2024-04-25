from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Expense, Category
from .forms import ExpensesForm


# Create your views here.

@login_required(login_url='/authentication/login/')
def index (request):

    expenses = Expense.objects.filter(owner=request.user)
    context = {
        'expenses' : expenses
    }
    
    return render(request,'expenses/index.html',context)


# @login_required(login_url='/authentication/login/')
# def add_expense (request):

#     categories = Category.objects.all()
#     context = {
#         'categories':categories,
#         'values' : request.POST
#     }

#     if request.method =='POST' :
#         amount = request.POST['amount']
#         description = request.POST['description']
#         category = request.POST['category']
#         date = request.POST['date']

#         if not amount :
#             messages.error(request, 'Amount Required')
#             return render(request,'expenses/add_expense.html',context)
        
#         if not description :
#             messages.error(request, 'Description Required')
#             return render(request,'expenses/add_expense.html',context)
        
#         if not category :
#             messages.error(request, 'Category Required')
#             return render(request,'expenses/add_expense.html',context)
        
#         if not date :
#             messages.error(request, 'Expense date Required')
#             return render(request,'expenses/add_expense.html',context)
        
#         Expense.objects.create(
#             amount = amount,
#             description = description,
#             category = category,
#             date = date,
#             owner = request.user,
#         )

#         messages.success(request, 'Expense Saved')
#         return render(request,'expenses/index.html',context)

    
#     return render(request,'expenses/add_expense.html',context)

    
@login_required(login_url='/authentication/login/')
def add_expense (request):

    if request.method =='POST' :
        form = ExpensesForm(request.POST)
        if form.is_valid :
            myform=form.save(commit=False)
            myform.owner = request.user
            myform.save()
            messages.success(request, 'Expense Succesfully Saved')
            return redirect ('expenses')
    else :
        form = ExpensesForm()
        
    context = {
        'form':form,
        'values' : request.POST,
    }

    return render(request,'expenses/add_expense.html',context)
    
    

@login_required(login_url='/authentication/login/')
def edit_expense (request,pk):

    expense = Expense.objects.get(id=pk)

    if request.method == 'POST' :
        form = ExpensesForm(request.POST,instance=expense)
        if form.is_valid() :
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            messages.success(request, 'Expense Succesfully Edited')
            return redirect ('expenses')
    else :
        form = ExpensesForm(instance=expense)

    context = {
        'form' : form
    }
    
    return render(request,'expenses/Edit_expense.html',context)
    
    

@login_required(login_url='/authentication/login/')
def delete_expense (request):
    pk = request.POST['pk']
    expense = Expense.objects.get(id=pk)
    if request.method == 'POST' :
        expense.delete()
        messages.error(request, 'Expense Succesfully Deleted')
    return redirect ('expenses')

# @login_required(login_url='/authentication/login/')
# def delete_expense (request):
#     pk = request.POST['pk']
#     expense = Expense.objects.get(id=pk)
#     if request.method == 'POST' :
#         expense.delete()
#         messages.error(request, 'Expense Succesfully Deleted')
    
#     expenses = Expense.objects.all()
#     page = render_to_string('expenses/includes/expenses-table.html', {'expenses':expenses })
#     return JsonResponse({'result':page})