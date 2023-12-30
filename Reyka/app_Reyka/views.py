from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from .models import Project,Project_task,Photo,User
from django.views.generic.list import ListView
from .form import Form,Registration,Login,RegistrationForm,LoginForm,Projectt,TaskCreateForm,TestForm
from django.views.generic.edit import CreateView,UpdateView,FormView
from django.urls import reverse_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.template.loader import render_to_string
from django.core.files import File
from pathlib import Path
from .serializers import UserSeriaLizer


class hh(TemplateView):
    template_name = 'hh.html'
    def post(self, request):
        data=request.POST
        #resp=render_to_string('responce.html',{'username':data['username'],'password':data['password'],'gmail':data['gmail']})
        with open('app_Reyka/static/images/file.png','wb') as photo:
            photo.write(request.FILES['photo'].read())
        path = Path('app_Reyka/static/images/file.png')
        with path.open(mode='rb') as img:
            file=File(img,name=img.name)
            photo=Photo(image=file)
            photo.save()
        return JsonResponse(1,safe=False)



class Home(ListView):
    template_name='home.html'
    model=Project
    paginate_by = 1

    # context_object_name='projects'
    #
    # def get_context_data(self, object_list):
    #     context=super().get_context_data(self,**kwargs)


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




class taskss(TemplateView):
    template_name = 'project.html'
    model= Project

    success_url = reverse_lazy('home')

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        project=Project.objects.get(id=self.kwargs['id'])
        tasks = Project_task.objects.filter(project_task=project)
        context ['project']=project
        context['tasks'] = tasks
        context['form'] = TaskCreateForm()
        return context

    def post(self, request,**kwargs):
        data=request.POST
        if len(data.keys()) == 4:
            project=Project.objects.get(id=self.kwargs['id'])
            task=Project_task(text=data['text'],status=True if data['status']=='on'else False,deadline=data['deadline'],project_task=project)
            task.save()
            project_task=render_to_string('responcee.html',{'i':task,'project':project})
            return JsonResponse(project_task,safe=False)
        if len(data.keys()) == 2:
            task=Project_task.objects.get(id=int(data['id']))
            resp = render_to_string('edit_form.html',{'form':TaskCreateForm(initial={'text':task.text,
                                                                                     'status':task.status,
                                                                                     'deadline':task.deadline})})
            return JsonResponse(resp,safe=False)

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
        return JsonResponse({'resp':'ok'},safe=False)


class bb(TemplateView):
    template_name = 'testss.html'

    def get(self, request, *args):
        user=User.objects.all()
        serializers=UserSeriaLizer(user,many=True)
        return JsonResponse(serializers.data,safe=False)
