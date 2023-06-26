from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from account.models import Register
from account.models import Categories
from account.models import EmployeeDetails

from account.forms import EmployeeAdd
import os

# Create your views here.


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        confirm_password = request.POST["confirm_password"]
        password = request.POST["password"]
        if password == confirm_password:
            if Register.objects.filter(username=username).exists():
                messages.info(request, "Username already taken.")
                return redirect("register")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "Email already taken.")
                return redirect("register")
            else:
                userRegister = Register(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )
                userRegister.save()
                messages.info(request, "Register successfully.")
        else:
            messages.info(request, "please check password.")
            return redirect("register")
        return redirect("/")
    else:
        return render(request, "register.html")


def login(request):
    if request.method == "POST":
        log_user = request.POST["username"]
        log_pass = request.POST["password"]
        print(log_user, log_pass)
        if log_user == "":
            messages.info(request, "Please enter username.")
            return redirect("/")
        elif log_pass == "":
            messages.info(request, "Please enter password.")
            return redirect("/")
        elif Register.objects.filter(username=log_user, password=log_pass).exists():
            return redirect("/home")
        else:
            messages.info(request, "Please enter valid credential.")
            return redirect("/")
    return render(request, "login.html")


def home_page(request):
    queryset = EmployeeDetails.objects.all()
    return render(request, "home.html", {"emp_details": queryset})


#     import random
#     import string

#     letters = string.ascii_lowercase
#     random_string = "".join(random.choice(letters) for i in range(10))
#     name, ext = os.path.splitext(filename)
#     return f"{name}_{random_string}{ext}"


def category_list(request):
    data = Categories.objects.select_related("CategoriesImg").all()
    for obj in data:
        # Access the related Table2 data using the foreign key relationship
        related_table2_data = obj.categories_img
        # Access the fields of Table1 and Table2
        field1 = obj.categories
        field2 = related_table2_data.image
        # Do something with the data
        print(f"Table1: {field1}, Table2: {field2}")
    return render(request, "category_list.html")


def add_employee(request):
    if request.method == "POST":
        email = request.POST["email"]
        phone_number = request.POST["phone"]
        if EmployeeDetails.objects.filter(phone=phone_number).exists():
            messages.info(request, "Phone already used.")
            return redirect("/add-employee")
        elif EmployeeDetails.objects.filter(email=email).exists():
            messages.info(request, "Email already taken.")
            return redirect("/add-employee")
        else:
            form = EmployeeAdd(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Register successfully.")
        else:
            print(form.errors)
        return redirect("/add-employee")
    else:
        return render(request, "add_employee.html")

def edit_user_details(request, id):
    employee_data = get_object_or_404(EmployeeDetails, id=id)
    if request.method == "POST":
        form = EmployeeAdd(request.POST, instance=employee_data)
        if form.is_valid():
            form.save()
            messages.info(request, "Employee details updated.")
            return redirect("/home")
        else:
            messages.info(request, "Employee details update failed.")
            return redirect("/home")
    return render(request, "add_employee.html", {"employee": employee_data})

def delete_emp(request, id):
    employee = get_object_or_404(EmployeeDetails, id=id)
    employee.delete()
    messages.info(request, "Employee record is deleted.")
    return redirect('/home')
