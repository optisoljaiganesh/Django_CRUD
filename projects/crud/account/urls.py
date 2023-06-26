from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
    path('home', views.home_page, name="home"),
    path('category-list', views.category_list, name="category_list"),
    path('add-employee', views.add_employee, name="add_employee"),
    path('edit/<int:id>/', views.edit_user_details, name='edit_user_details'),
    path('delete/<int:id>/', views.delete_emp, name='delete_emp'),

] 