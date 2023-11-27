from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .models import Project,Project_task
from django.views.generic.list import ListView
from .form import Form,Registration,Login,RegistrationForm,LoginForm,Projectt,TaskCreateForm,TestForm
from django.views.generic.edit import CreateView,UpdateView,FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

class Home(ListView):
    template_name='home.html'
    model=Project
    context_object_name='projects'

    def get_context_data(self, object_list):
        context=super().get_context_data(self,**kwargs)


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




class Register(CreateView):
    template_name = 'newregister.html'
    model= User
    form_class=RegistrationForm
    success_url = reverse_lazy('home')




class LoginPage(LoginView):
    template_name = 'newlogin.html'
    model= User
    form_class=LoginForm
    redirect_authenticated_user=True




class Projects(CreateView):
    template_name = 'create_project.html'
    model= Project
    form_class=Projectt
    success_url = reverse_lazy('home')

class projects_redict(UpdateView):
    template_name = 'project_redict.html'
    model= Project
    form_class=Projectt
    success_url = reverse_lazy('home')

class task_redict(UpdateView):
    template_name = 'task_redict.html'
    model= Project_task
    form_class=TaskCreateForm
    success_url = reverse_lazy('home')


def task(request,**kwargs):
    project=Project.objects.get(id=kwargs['id'])
    if request.method =='POST':
        form=TaskCreateForm(request.POST)
        if form.is_valid():
            text_task=form.cleaned_data['text_task']
            status = form.cleaned_data['status']
            deadline = form.cleaned_data['deadline']
            task=Project_task(text_task=text_task,status=status,deadline=deadline,project_task=project)
            task.save()
            return redirect('/')
    else:
        tasks=Project_task.objects.filter(project_task=project)
        form=TaskCreateForm()
        context = {'project': project,'tasks': tasks,'form': form}
        return render(request, 'task.html', context)


class TestsForm(FormView):
    template_name = 'test.html'
    form_class=TestForm
    success_url = reverse_lazy('/')


    def form_valid(self,form):
        response=HttpResponse()
        response.set_cookie('name',form.cleaned_data['name'])
        return super().form_valid(form)
        request.COOKIES['name']


class gob(TemplateView):
    template_name = 'testss.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='gob'
        return context

    def post(self, request):
        data=request.POST
        print(data['text'])


