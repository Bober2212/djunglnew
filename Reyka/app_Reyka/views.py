from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')


def page2(request):
    return HttpResponse('Hello')

def about(request):
    return render(request,'about.html')

def about_me(request):
    return render(request,'about_me.html')

def page3(request):
    name = 'Bob'

    age = '10'

    pridvishe = 'Bobovish'
    context = {'name_user': name,'age_user': age,'pridvishe_user': pridvishe}
    return render(request, 'page3.html', context)

def page4(request):
    name = ['Bob','fdg','Axs','Dota','Huskar','mamont','Giena','cucumber','apple','green',]
    context = {'name_user': name}
    return render(request, 'page4.html', context)