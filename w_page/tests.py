<br>
<div class="container">
  <ul id="tabs-swipe-demo" class="tabs">
    <li class="tab col s3 blue-text"><a class="active indigo white-text" href="#test-swipe-1">Entrar como paciente</a></li>
    <li class="tab col s3"><a  class="purple white-text" href="#test-swipe-2">Entrar como doctor</a></li>
  </ul>
  <div id="test-swipe-1" class="col s12 white">
    

    <div class="row "> 
      <form class="col s8 " method="POST">{% csrf_token %}

          <div class="">
            <br>

            <div class="col s4">
                <img src="https://w0.peakpx.com/wallpaper/834/159/HD-wallpaper-anime-aesthetic-aesthetic-anime.jpg" alt="" width="300" height="360">
                
            </div>

            <div class="col s4">
                <h4 class="header indigo darken-4 white-text center">Pacientes</h4>
            </div>

            <div class="input-field col s4">
              <input name="user_id" id="email" type="text" class="validate">
              <label for="email">Id de Usuario</label>
            </div>
  
            <div class="input-field col s4">
              <input name="user_password" id="email" type="text" class="validate">
              <label for="email">Contraseña</label>
            </div>

  
      
            <div class="center">
              <button class="btn indigo darken-4 col s4 container" name="person" type="submit">Entrar</button>
            </div>

            <div class="center">
              <button class="btn indigo darken-4 col s4 container" name="person" type="submit">Volver</button>
            </div>
               </div>
      </form>
    </div>


  </div>
  <div id="test-swipe-2" class="col s12 white">

    <div class="row ">

    
  
      <form class="col s12 " method="POST">{% csrf_token %}

          <div class="">
            <br>

            <div class="col s6">
                <img src="https://img.freepik.com/free-vector/hand-drawn-abstract-repetitive-leaves-pattern_23-2148996044.jpg?w=740&t=st=1656445340~exp=1656445940~hmac=f5f33a7c4013158b70c1260a807c7c08c5b85a6c968159e91e5533198f4d638d" alt="" width="400" height="360">
                
            </div>

            <div class="col s6">
                <h3 class="header">Doctores</3>
            </div>

            <div class="input-field col s4">
              <input name="user_id" id="email" type="text" class="validate">
              <label for="email">Id de Usuario</label>
            </div>
  
            <div class="input-field col s4">
              <input name="user_password" id="email" type="text" class="validate">
              <label for="email">Contraseña</label>
            </div>

            <p class="col s6" style="visibility: hidden">none text</p>
      
            <div class="center">
              <button class="btn indigo darken-4 col s4 container" name="doctor" type="submit">Entrar</button>
            </div>
               </div>
      </form>
    </div>


  </div>
</div>