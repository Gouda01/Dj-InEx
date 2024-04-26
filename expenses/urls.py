from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.ExpenseList.as_view(), name='expenses'),
    path('add_expense', views.add_expense, name='add_expense'),
    path('edit_expense/<int:pk>', views.edit_expense, name='edit_expense'),
    path('delete_expense', views.delete_expense, name='delete_expense'),

    path('search-expenses', csrf_exempt(views.search_expenses), name='search-expenses'),
]
