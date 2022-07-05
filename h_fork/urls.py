"""h_fork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home_view ,who
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('home/', home_view.as_view(), name = "home"),
    
    path('api/', include('w_page.urls')),
    
    path('login_user/', views.login_user_view ),
    
    path('login_doctor/', views.login_doctor_view ),
    
    path('who/', who.as_view()),
    
    #path('register_user/' , views.create_patient),
    
    #path('register_doctor/' , views.create_doctor),
    
    path('user/' , views.user_view1),
    
    path('user/<int:id>' , views.user_view),
    
    path('doctor/' , views.doctor_view1),
    
    path('doctor/<int:id>' , views.doctor_view),
    
    path('user_created/' , views.user_created),
    
    path('user_created/<int:id>' , views.user_created_id),
    
    path('doctor_created/' , views.doctor_created),
    
    path('doctor_created/<int:id>' , views.doctor_created_id),
    
    path('register/' , views.create_all),
    
    path('login/' , views.login_all),  
    
    path('user_found/' , views.user_found),
    
    path('user_found/<int:id>' , views.user_found_id),  
    
    path('buscar_paciente/' , views.buscar_paciente),
    
    path('buscar_registro/' , views.buscar_registro),          
    
    path('enviar_diagnostico/' , views.enviar_diagnostico),  
    
    path('actualizar_doctor/' , views.actualizar_doctor),
    
    path('actualizar_doctor/<int:id>' , views.actualizar_doctor_id),
    
    path('mostrar_paciente/<int:id>' , views.mostrar_paciente),   
    
    path('mostrar_registro/<int:id>' , views.mostrar_registro),   
    
]  

