from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .models import Project,Project_task
from .form import Form,Registration,Login,RegistrationForm,LoginForm,Projectt,TaskCreateForm
def home(request):
    projects=Project.objects.all()
    contex={'projects':projects}
    return render(request,'home.html',contex)


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
    form=Form()
    name = ['Bob','fdg','Axs','Dota','Huskar','mamont','Giena','cucumber','apple','green',]
    context = {'name_user': name,'form':form}
    return render(request, 'page4.html', context)


def page5(request):
    if request.method == 'POST':
        form=Form(request.POST)
        if form.is_valid():
            surname = form.cleaned_data['surname']
            phone_number = form.cleaned_data['phone_number']
            gmail = form.cleaned_data['gmail']

            contexts = {'surname': surname, 'phone_number': phone_number
                , 'gmail': gmail, 'form': form}
            return render(request, 'page5.html',contexts)
    else:
        form=Form()
    context = {'form':form}
    return render(request, 'page5.html', context)


def logins(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            surname = form.cleaned_data['surname']
            phone_number = form.cleaned_data['phone_number']
            gmail = form.cleaned_data['gmail']
            password = form.cleaned_data['password']
            contexts = {'surname': surname, 'phone_number': phone_number
                , 'gmail': gmail, 'form': form, 'password': password}
            return render(request, 'page5.html', contexts)
    else:
        form = Login()
    context = {'form': form}
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            surname = form.cleaned_data['surname']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']
            gmail=form.cleaned_data['gmail']
            contexts = {'surname': surname, 'phone_number': phone_number
                , 'gmail': gmail, 'form': form, 'password': password}
            return render(request, 'page5.html', contexts)
    else:
        form = Registration()
    context = {'form': form}
    return render(request, 'register.html', context)


def newregister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user=User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            login(request,user)
            return redirect('/')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'newregister.html', context)


def newlogin(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print('1')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user= authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return redirect('/loginn')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'newlogin.html', context)


def projects(request):
    if request.method == 'POST':
        form = Projectt(request.POST)
        if form.is_valid():
            name_project = form.cleaned_data['name_project']
            level = form.cleaned_data['level']
            project=Project(name_project=name_project, level=level)
            project.save()
            return redirect('/')
    else:
        form = Projectt()
    context = {'form': form}
    return render(request, 'create_project.html', context)


def task(request,**kwargs):
    project=Project.objects.get(id=kwargs['id'])
    if request.method =='POST':
        form=TaskCreateForm()
        if form.is_valid():
            text_task=form.cleaned_data['text_task']
            status = form.cleaned_data['status']
            deadline = form.cleaned_data['deadline']
            task=Project_task(text_task=text_task,status=status,deadline=deadline)
            task.save()
            return redirect('/')
    else:
        tasks=Project_task.objects.filter(project_task=project)
        form=TaskCreateForm()
        context = {'project': project,'tasks': tasks,'form': form}
    return render(request, 'task.html', context)

