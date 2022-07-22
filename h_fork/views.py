from django.views.generic import View

from django.http import HttpResponse

from django.shortcuts import render, redirect

from w_page.models import Person, Patient, Doctor, DoctorAcount, VitalSigns

from w_page.models import PatientDiagnostic, PhoneNumbers, UserAccount

import json

from django.http import JsonResponse

from w_page.forms import Patient_form, Doctor_form

import requests, time



def create_all(request):

    return render(request, 'main/register.html', {})

def login_all(request):
    return render(request, 'main/login.html')


class home_view(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "main/index.html", context)

class login_user(View):
    def get(self, request, *args, **kwargs):
        
        context={

        }
        return render(request, 'user/login_user.html', context)

class login_doctor(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'login_doctor.html', context)

class who(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'main/who.html', context)

def login_user_view(request):
    msg=""
    if request.method == "POST":
        uid = request.POST['user_id']
        upassword = request.POST['user_password']
        if (uid != 0 and upassword != 0 ):
            uacount=list(UserAccount.objects.filter(user_account_id=uid).values())
            upass = list(UserAccount.objects.filter(user_password=upassword).values())
            if len(uacount) > 0 and len(upass) > 0:
                #data= datas[0]
                msg = "Parece que los datos ingresados son correctos"
                user_view(request, uid)
                return redirect('/user/'+ str(uid))
            else:
                msg = "Parece que los datos ingresados son incorrectos"
            
                
            
        else:
            msg = "Parece que los datos ingresados son incorrectos"

            #return redirect('/login_user.html/')
    context={
        'msg': msg
    }
    return render(request, 'user/login_user.html', context)

def login_doctor_view(request):
    msg = ""
    if request.method == "POST":
        uid = request.POST['user_id']
        upassword = request.POST['user_password']
        if (uid != 0 and upassword != 0 ):
            uacount=list(DoctorAcount.objects.filter(doctor_account_id=uid).values())
            upass = list(DoctorAcount.objects.filter(doctor_password=upassword).values())
            if len(uacount) > 0 and len(upass) > 0:
                #data= datas[0]
                udata = {'msg': 'success'}
                msg = "correo y contraseña coinciden"
                doctor_view(request, uid)
                return redirect('/doctor/'+ str(uid))
                print(udata)
            else:
                udata = {'msg': 'error'}
                msg = "Parece que el correo o la contraseña no coinciden"
                
            #return HttpResponse(udata['msg'])
        else:
            data = {'message': 'not vitals registered'}

            # return HttpResponse(data)
      
    context={
        'mensaje' : msg
    }

    return render(request, 'login_doctor.html', context)

def doctor_view(request, id):
    #pull data from third party rest api
    #id = request.GET.get('id')
    response = requests.get('http://localhost:8000/api/persons/'+str(id))
    response2 = requests.get('http://localhost:8000/api/vitals/'+str(id)) 
    response3 = requests.get('http://localhost:8000/api/diagnostic/'+str(id)) 
    response4 = requests.get('http://localhost:8000/api/doctor_accounts/'+str(id))
    
    
    #convert reponse data into json
    users = response.json()
    vitals = response2.json()
    diagnostic = response3.json()
    titles = response4.json()
    
    
    #all_data = json.loads(users)
    
    context = {
        'data': users,
        'vitals': vitals,
        'diagnostic': diagnostic,
        'titles': titles
    }
    #print(users)
    return render(request, 'doctor/doctor.html', context)


    
    return render(request, 'doctor/doctor.html')

def user_view(request, id):
    #pull data from third party rest api
    #id = request.GET.get('id')
    response = requests.get('http://localhost:8000/api/persons/'+str(id))
    response2 = requests.get('http://localhost:8000/api/vitals/'+str(id)) 
    response3 = requests.get('http://localhost:8000/api/diagnostic/'+str(id)) 
    
    #convert reponse data into json
    users = response.json()
    vitals = response2.json()
    diagnostic = response3.json()
    
    oxigen = vitals
    
    #all_data = json.loads(users)
    
    context = {
        'data': users,
        'vitals': vitals,
        'diagnostic': diagnostic,
    }
    #print(users)
    return render(request, 'user/user.html', context)

def user_view1(request):
    
    return render(request, 'user/user.html')

def doctor_view1(request):
    return render(request, 'doctor/doctor.html')

def user_created(request):
    return render(request, 'user/user_created.html')

def user_created_id(request, id):
    response = requests.get('http://localhost:8000/api/user_accounts/'+str(id))
    
    #convert reponse data into json
    users = response.json()
    
    context = {
        'data': users,
    }
    #print(users)
    
    return render(request, 'user/user_created.html', context)

def doctor_created(request):
    return render(request, 'doctor/doctor_created.html')

def doctor_created_id(request, id):
    response = requests.get('http://localhost:8000/api/doctor_accounts/'+str(id))
    
    #convert reponse data into json
    users = response.json()
    
    context = {
        'data': users,
    }
    #print(users)
    return render(request, 'doctor/doctor_created.html', context)

def user_found(request):
    return render(request, 'user/user_found.html')

def user_found_id(request, id):
    response = requests.get('http://localhost:8000/api/patients/'+str(id))
    
    #convert reponse data into json
    users = response.json()
    
    context = {
        'data': users,
    }
    #print(users)
    return render(request, 'user/user_found.html', context)

# Forms de busca de datos de parte del doctor
def buscar_paciente(request):
    if request.method == 'POST':    
        uid = request.POST['user_id']
        if (uid != 0  ):
            uacount=list(UserAccount.objects.filter(user_account_id=uid).values())
            if len(uacount) > 0:
                #data= datas[0]
                msg = "Parece que los datos ingresados son correctos"
                mostrar_paciente(request, uid)
                return redirect('/mostrar_paciente/'+ str(uid))
            else:
                msg = "Parece que los datos ingresados son incorrectos"           
        else:
            msg = "Parece que los datos ingresados son incorrectos"
    
    
    return render(request, 'doctor/buscar_paciente.html')

def buscar_registro(request):
    if request.method == 'POST':    
        uid = request.POST['user_id']
        if (uid != 0  ):
            uacount=list(VitalSigns.objects.filter(patient_id=uid).values())
            if len(uacount) > 0:
                #data= datas[0]
                msg = "Parece que los datos ingresados son correctos"
                mostrar_registro(request, uid)
                return redirect('/mostrar_registro/'+ str(uid))
            else:
                msg = "Parece que los datos ingresados son incorrectos"           
        else:
            msg = "Parece que los datos ingresados son incorrectos"
            
    return render(request, 'doctor/buscar_registros.html')

def enviar_diagnostico(request, id):   
    response = requests.get('http://localhost:8000/api/doctors/'+str(id))
    
    users = response.json()
    
    context = {
        'data': users,
    }
    
    return render(request, 'doctor/enviar_diagnostico.html', context)
    

def actualizar_doctor(request):
    return render(request, 'doctor/actualizar_doctor.html')

def actualizar_doctor_id(request, id):
    response = requests.get('http://localhost:8000/api/persons/'+str(id))
    
    users = response.json()
    
    context = {
        'data': users,
    }
    
    return render(request, 'doctor/actualizar_doctor.html', context)


def actualizar_paciente(request):
    return render(request, 'user/update_user.html')


def actualizar_paciente_id(request, id):
    response = requests.get('http://localhost:8000/api/persons/' + str(id))

    users = response.json()

    context = {
        'data': users,
    }

    return render(request, 'user/update_user.html', context)

# Vistas de datos que busca el doctor

def mostrar_paciente(request, id):
    response = requests.get('http://localhost:8000/api/patients/'+str(id))
    
    #convert reponse data into json
    users = response.json()
    
    context = {
        'data': users,
    }
    #print(users)
    return render(request, 'doctor/mostrar_paciente.html', context)

def mostrar_registro(request, id):
    response = requests.get('http://localhost:8000/api/vitals/'+str(id))
    response2 = requests.get('http://localhost:8000/api/diagnostic/'+str(id))
    
    #convert reponse data into json
    users = response.json()
    diag = response2.json()
    
    context = {
        'vitals': users,
        'diagnostic': diag
    }
    #print(users)
    return render(request, 'doctor/mostrar_registro.html', context)

def listado_pacientes(request, id):

    return render(request, 'doctor/listado_pacientes.html')

def listado_pacientes_id(request, id):
    response = requests.get('http://localhost:8000/api/persons/' + str(id))

    users = response.json()

    #person_id = Person.objects.filter(person_id=person_id)
    ids = Person.objects.values_list('person_id', flat=True)

    # list method get ids without parse the returning queryset

    print(list(ids))

    context = {
        'data': users,
        'patients': ids
    }
    return render(request, 'doctor/listado_pacientes.html', context)