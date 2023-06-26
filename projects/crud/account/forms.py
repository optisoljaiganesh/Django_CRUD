from django  import forms
from account.models import Register
from account.models import EmployeeDetails


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class EmployeeAdd(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']