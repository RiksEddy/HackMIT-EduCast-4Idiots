from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
# Create your views here.

def landing_page(request):

     return render(request,'portal/landing_page.html')

def student_signup(request):
     if request.method=='POST':
          form = student_signup_form(request.POST)
          if form.is_valid():
               user=User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
          )
               new_profile= Profile(
                    identity = user,
                    department=form.cleaned_data['department'],
                    is_student = True,
                    is_teacher = False,
               )
               new_profile.save()
               return redirect('/')
          else:
               return HttpResponse('<h1>Try Again</h1>')
     else:
          form = student_signup_form()
          return render(request, 'portal/student_signup.html', {'form': form})

def teacher_signup(request):
     if request.method=='POST':
          form = teacher_signup_form(request.POST)
          if form.is_valid():
               user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
               )
               new_profile = Profile(
                    identity=user,
                    department=form.cleaned_data['department'],
                    is_student=False,
                    is_teacher=True,
               )
               user.save()
               new_profile.save()
               return redirect('/')
          else:
               return HttpResponse('<h1>Try Again</h1>')
     else:
        form = student_signup_form()
     return render(request, 'portal/teacher_signup.html', {'form': form})


def user_login(request):
     if request.method == 'POST':
          form = UserLoginForm(request.POST)
          if form.is_valid():
               username = request.POST['username']
               password = request.POST['password']
               user = authenticate(username=username, password=password)
               if user:
                    if user.profile.is_student:
                         login(request, user)
                         return redirect('student_dashboard')
                    elif user.profile.is_teacher:
                         login(request, user)
                         return redirect('teacher_dashboard')
               else:
                    return render(request, 'portal/inactiv_account.html')
     else:
          form = UserLoginForm()

     context = {
          'form': form,
     }
     return render(request, 'portal/login.html', context)

def user_logout(request):
	django_logout(request)
	return redirect('/')


def teacher_dashboard(request):
     if request.method == 'POST':
          form = DocumentForm(request.POST, request.FILES)
          if form.is_valid():
               form.save(commit=True)
               # asd
               return render(request, 'portal/teacher_dashboard.html')
     else:
          form = DocumentForm()
     return render(request, 'portal/teacher_dashboard.html', {
          'form': form
     })


def student_dashboard(request):
     documents = Document.objects.all()
     return render(request, 'portal/student_dashboard.html', {'documents': documents})
