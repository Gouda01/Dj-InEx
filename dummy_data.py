import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from django.contrib.auth.models import User

from expenses.models import Expense, Category



def seed_categories (n):
    fake = Faker()

    for _ in range(n):
        Category.objects.create (
            name = fake.name(),
        )
    print(f"{n} Categories was added successfuly")


def seed_expenses(n):
    fake = Faker()
    
    categories = Category.objects.all()
    users = User.objects.all()

    for _ in range(n):
        Expense.objects.create (
            amount = round(random.uniform(1000.00,100000.00),2),
            description = fake.text(max_nb_chars=100),
            owner = users[random.randint(0,len(users)-1)],
            category = categories[random.randint(0,len(categories)-1)],
                      
        )
    print(f"{n} Products was added successfuly")




# seed_categories(5)
seed_expenses(500)
