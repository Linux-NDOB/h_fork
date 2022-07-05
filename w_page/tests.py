def create_patient(request):
    if request.method == "POST":
        form = Patient_form(request.POST)
        if form.is_valid():
            try:
                form.save()
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
        form = Patient_form
    return render(request, 'user/register_user.html', {'form':form})

def create_doctor(request):
    if request.method == "POST":
        form = Doctor_form(request.POST)
        if form.is_valid():
            try:
                form.save()
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
    else:
        form = Doctor_form
    return render(request, 'register_doctor.html', {'form':form})


<ul class="collection">
      
      <li class="collection-item avatar">
      <i class="material-icons circle teal">format_list_bulleted</i>
        <span class="title">Buscar Paciente</span>
        <p>Buscar datos de un paciente por numero de Cedula
        </p>
        <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
      </li>
      <li class="collection-item avatar">
        <i class="material-icons circle red">unfold_more</i>
        <span class="title">Buscar Registro</span>
        <p>Buscar Registro de Paciente por numero de Cedula</p>
        <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
      </li>
      <li class="collection-item avatar">
        <i class="material-icons circle yellow">mail</i>
        <span class="title">Enviar diagnostico</span>
        <p>Enviar diagnostico a paciente por medio de su cedula
        </p>
        <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
      </li>
    </ul>
    
    
    
    
    
    
    
    
    
    
    
    
    
    <div class="container">

  <h4 class="purple darken-4 center white-text">Datos de Doctor</h4>
  <ul class="collection">
    
    <li class="collection-item avatar">
    <i class="material-icons circle indigo">person</i>
      <span class="title">Nombres</span>
      <p>Primer nombre: {{data.person.name}} <br>
         Segundo nombre: {{data.person.second_name}}
      </p>
      <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
    </li>
    <li class="collection-item avatar">
      <i class="material-icons circle blue">account_circle</i>
      <span class="title">Apellidos</span>
      <p>Primer apellido: {{data.person.lastname}}<br>
         Segundo apellido: {{data.person.second_lastname}}
      </p>
      <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
    </li>
    <li class="collection-item avatar">
      <i class="material-icons circle purple">person_pin</i>
      <span class="title">Datos</span>
      <p>Cedula: {{data.person.person_id}} <br>
         Edad: {{data.person.age}} <br>
      </p>
      <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
    </li>
  </ul>
</div>
      


<div class="container">

    <h4 class="pink  center white-text">Opciones de Doctor</h4>
    
  </div>

 <!-- Modal Trigger -->
 <div class="container center">
  <a class="waves-effect waves-light btn modal-trigger indigo" href="#modal1">Mostrar opciones</a>
  <br>
 </div>
<br>
 <!-- Modal Structure -->
 <div id="modal1" class="modal bottom-sheet">
   <div class="modal-content">
     <h4>Modal Header</h4>
     <ul class="collection">
      
      <li class="collection-item avatar">
      <i class="material-icons circle teal">format_list_bulleted</i>
        <span class="title">Buscar Paciente</span>
        <p>Buscar datos de un paciente por numero de Cedula
        </p>
        <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
      </li>
      <li class="collection-item avatar">
        <i class="material-icons circle red">unfold_more</i>
        <span class="title">Buscar Registro</span>
        <p>Buscar Registro de Paciente por numero de Cedula</p>
        <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
      </li>
      <li class="collection-item avatar">
        <i class="material-icons circle yellow">mail</i>
        <span class="title">Enviar diagnostico</span>
        <p>Enviar diagnostico a paciente por medio de su cedula
        </p>
        <a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>
      </li>
    </ul>
   </div>
   <div class="modal-footer">
     <a href="#!" class="modal-close waves-effect waves-green btn-flat">Cerrar</a>
   </div>
 </div>

</div>


<div class="col s4">
                <img src="https://www.juanmacivico87.com/wp-content/uploads/que-es-material-design.png" alt="">
                
            </div>


<div class="container">
  <ul class="collapsible popout">
    <li class="">
      <div class="collapsible-header"><i class="material-icons">person</i>Entrar como Paciente/Usuario</div>
      <div class="collapsible-body">
        <form action="" method="POST" class="col s12 container" id="post-form">{% csrf_token %}
          <div class="input-field">
            <input name="user_id" id="email" type="text" class="validate">
            <label for="email">Id de Usuario</label>
          </div>

          <div class="input-field">
            <input name="user_password" id="email" type="text" class="validate">
            <label for="email">Contraseña</label>
          </div>
          
  
          <div class="center">
            <button class="btn indigo darken-4" name="person" type="submit">Entrar</button>
          </div>
        </form>
      </div>
    </li>
    <li>
      <div class="collapsible-header"><i class="material-icons">medication</i>Entrar como Doctor</div>
      <div class="collapsible-body">
        <form action="" method="POST" class="col s12 container" id="post-form">{% csrf_token %}
            <div class="input-field">
              <input name="user_id" id="email" type="text" class="validate">
              <label for="email">Id de Doctor</label>
            </div>

            <div class="input-field">
              <input name="user_password" id="email" type="text" class="validate">
              <label for="email">Contraseña</label>
            </div>
          
          <div class="center">
            <button class="btn indigo darken-4" name="doctor" type="submit">Entrar</button>
          </div>
        </form>
      </div>       
</li>
  </ul>
</div>










{% extends 'base.html' %}

{% block title %} Registro {% endblock %}

{% block content%} 


<div class="container">
  <div class="carousel carousel-slider center">
    <div class="carousel-fixed-item center">
      <a class="btn waves-effect white black-text darken-text-2 white">Inicio</a>
    </div>
    <div class="carousel-item blue white-text" href="#one!">
      <h2>First Panel</h2>
      <p class="white-text">This is your first panel</p>
    </div>
    <div class="carousel-item indigo white-text" href="#two!">
      <h2>Second Panel</h2>
      <p class="white-text">This is your second panel</p>
    </div>
    <div class="carousel-item green white-text" href="#three!">
      <h2>Third Panel</h2>
      <p class="white-text">This is your third panel</p>
    </div>
    <div class="carousel-item teal white-text" href="#four!">
      <h2>Fourth Panel</h2>
      <p class="white-text">This is your fourth panel</p>
    </div>
  </div>
</div>


<div class="container">
  <ul class="collapsible popout">
    <li class="">
      <div class="collapsible-header"><i class="material-icons">person</i>Registrarse como Paciente/Usuario</div>
      <div class="collapsible-body">
        <form action="" method="POST" class="col s12 container" id="post-form">{% csrf_token %}
       
          {{expectedphraseform}}
  
          <div class="center">
            <button class="btn indigo darken-4" name="person" type="submit">Registrarse</button>
          </div>
        </form>
      </div>
    </li>
    <li>
      <div class="collapsible-header"><i class="material-icons">medication</i>Registrarse como Doctor</div>
      <div class="collapsible-body">
        <form action="" method="POST" class="col s12 container" id="post-form">{% csrf_token %}
         
            <div class="input-field">
              <input name="title" id="email" type="text" class="validate">
              <label for="email">Titulo</label>
            </div>
          
       
          {{bannedphraseform}}
  
          <div class="center">
            <button class="btn indigo darken-4" name="doctor" type="submit">Registrarse</button>
          </div>
        </form>
      </div>       
</li>
  </ul>
</div>