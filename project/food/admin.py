from django.contrib import admin
from food.models import *

# Register your models here.

admin.site.register([Place, Restaurant, Pizza, Topping, Waiter])