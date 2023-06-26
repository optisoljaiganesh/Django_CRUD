from django.shortcuts import render

from idea.models import TestModel
from idea.models import IdeaModel

# Create your views here.



def index(request):
    # return HttpResponse("<h1>Hollo world!</h1>")
    return render(request,'index.html')


def welcome(request):
    # info = TestModel()
    # info.name = "jai"
    # info.age = 23
    # info.address= "Trichy"
    # info.phone = 7339274912
    # info.active =False


    # info2 = TestModel()
    # info2.name = "jai ganesh"
    # info2.age = 25
    # info2.address= "Chennai"
    # info2.phone = 7339274912
    # info.active =True

    # info3 = TestModel()
    # info3.name = "Leo"
    # info3.age = 23
    # info3.address= "Trichy"
    # info3.phone = 7339274912
    # info.active =True

    # allInfo = [ info, info2, info3]

    allInfo = IdeaModel.objects.all()

    return render(request,'welcome.html', {'info' : allInfo})
    

