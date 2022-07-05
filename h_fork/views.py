from django.views.generic import View

from django.http import HttpResponse

from django.shortcuts import render, redirect

from w_page.models import Person, Patient, Doctor, DoctorAcount, VitalSigns

from w_page.models import PatientDiagnostic, PhoneNumbers, UserAccount

import json

from django.http import JsonResponse

from w_page.forms import Patient_form, Doctor_form

import requests

def create_all(request):
    expectedphraseform = Patient_form(request.POST)
    bannedphraseform = Doctor_form(request.POST)
    if request.method == 'POST' and 'doctor' in request.POST:    
        if  bannedphraseform.is_valid():
            try:
                bannedphraseform.save()
                person_id = request.POST['person_id']
                username = request.POST['name']
                email = request.POST['person_id']+"@gmail.com"
                title = request.POST['title']
                password =  username[0:3] + person_id[0:3] 
                
                Doctor.objects.create(doctor_id=person_id, 
                                    person = Person.objects.get(person_id=person_id),
                                    title=title)
                
                DoctorAcount.objects.create(doctor_account_id=person_id,doctor = Doctor.objects.get(doctor_id=person_id),
                                        doctor_email=email, doctor_password= password, doctor_username=request.POST['name'])
                
                doctor_created_id(request, person_id)
                return redirect('/doctor_created/'+ str(person_id))
            except:
                pass
        
    if request.method == 'POST' and 'person' in request.POST:  
            try:
                expectedphraseform.save()
                person_id = request.POST['person_id']
                username = request.POST['name']
                email = request.POST['person_id']+"@gmail.com"
                password =  username[0:3] + person_id[0:3] 

                
                Patient.objects.create(patient_id=person_id, 
                                    person = Person.objects.get(person_id=person_id))
                
                UserAccount.objects.create(user_account_id=person_id,patient = Patient.objects.get(patient_id=person_id),
                                        user_email=email, user_password= password, username=request.POST['name'])
                
                user_created_id(request, person_id)
                return redirect('/user_created/'+ str(person_id))
            except:
                pass
        
        
    else:
        bannedphraseform = Doctor_form()
        expectedphraseform = Patient_form()
    return render(request, 'main/register.html', {'bannedphraseform':bannedphraseform, 'expectedphraseform':expectedphraseform})

def login_all(request):
    if request.method == 'POST' and 'person' in request.POST:    
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
    
    msg = ""
    if request.method == "POST" and 'doctor' in request.POST:
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
            #return redirect('/login_user.html/')
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

def enviar_diagnostico(request):
    if request.method == 'POST':    
        uid = request.POST['patient_id']
        if (uid != 0  ):
            uacount=list(Patient.objects.filter(patient_id=uid).values())
            if len(uacount) > 0:
                jd = request.POST
                msg = "Parece que los datos ingresados son correctos"
                PatientDiagnostic.objects.create(diagnostic_id=jd['diagnostic_id'], 
                                    diagnostic_text=jd['diagnostic_text'], 
                                    patient = Patient.objects.get(patient_id=jd['patient_id']),
                                    doctor = Doctor.objects.get(doctor_id=jd['doctor_id'])
                                    )
                
                return redirect(request.META.get('HTTP_REFERER'))

            else:
                msg = "Parece que los datos ingresados son incorrectos"           
        else:
            msg = "Parece que los datos ingresados son incorrectos"
    
    return render(request, 'doctor/enviar_diagnostico.html')

def actualizar_doctor(request):
    return render(request, 'doctor/actualizar_doctor.html')

def actualizar_doctor_id(request, id):
    response = requests.get('http://localhost:8000/api/doctors/'+str(id))
    if request.method == 'POST':    
        uid = request.POST['person_id']
        if (uid != 0  ):
            uacount=list(Person.objects.filter(person_id=uid).values())
            if len(uacount) > 0:
                jd = request.POST
                person = Person.objects.get(person_id=uid)
                person.person_id = jd['person_id']
                person.name = jd['name']
                person.second_name = jd['second_name']
                
                person.lastname = jd['lastname']
                person.second_lastname = jd['second_lastname']
                person.age = jd['age']
                   
                person.save()
                
                return redirect(request.META.get('HTTP_REFERER'))

            else:
                return redirect(request.META.get('HTTP_REFERER'))
                msg = "Parece que los datos ingresados son incorrectos"           
        else:
            msg = "Parece que los datos ingresados"

    users = response.json()
    
    context = {
        'data': users,
    }
    
    return render(request, 'doctor/actualizar_doctor.html', context)

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