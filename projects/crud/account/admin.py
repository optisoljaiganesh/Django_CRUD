from django.contrib import admin

# Register your models here.
from .models import Register
from .models import Categories
from .models import EmployeeDetails
# from .models import CategoriesImg

admin.site.register(Register)
admin.site.register(Categories)
admin.site.register(EmployeeDetails)
# admin.site.register(CategoriesImg)