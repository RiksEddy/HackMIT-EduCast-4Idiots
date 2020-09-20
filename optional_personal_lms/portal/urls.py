from django.contrib import admin
from . import views
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing_page,name='landing_page'),
    path('student_signup', views.student_signup, name='student_signup'),
    path('teacher_signup', views.teacher_signup,  name='teacher_signup'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('teacher_dashboard', views.teacher_dashboard, name='teacher_dashboard'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard')
]

