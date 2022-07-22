console.log("im here");

let d = document;

// Login Form fields and buttons
let user_login_field = d.getElementById("user_login_field");

let user_login_password_field = d.getElementById("login_password_field");

let user_login_button = d.getElementById("user_login_button");


// Login Form fields and buttons
let doctor_login_field = d.getElementById("doctor_login_field");

let doctor_login_password_field = d.getElementById("doctor_password_field");

let doctor_login_button = d.getElementById("doctor_login_button");

// Login User
function validate_user() {
    let user_id = user_login_field.value;
    let user_password = user_login_password_field.value;

    if (user_id == '') {
        M.toast({ html: 'Campo de cedula vacio!' });
    } if (user_password == '') {
        M.toast({ html: 'Campo de contrasena vacio!' });
    } if (user_id != '' && user_password != '') {
        fetch('http://localhost:8000/api/user_accounts/' + user_id)
            .then(response => response.json())
            .then(data => {
                if (typeof data.user_account == 'undefined') {
                    M.toast({ html: 'Usuario no registrado en la base de datos!' });
                } else if (user_id == data.user_account.patient_id && user_password == data.user_account.user_password) {
                    location.href = '/user/' + user_id;
                }
                else {
                    M.toast({ html: 'Error en usuario o contrasena!' });
                }
            });
    }
}


// Login Doctor
function validate_doctor() {
    let doctor_id = doctor_login_field.value;
    let doctor_password = doctor_login_password_field.value;

    if (doctor_id == '') {
        M.toast({ html: 'Campo de cedula vacio!' });
    } if (doctor_password == '') {
        M.toast({ html: 'Campo de contrasena vacio!' });
    } if (doctor_id != '' && doctor_password != '') {
        fetch('http://localhost:8000/api/doctor_accounts/' + doctor_id)
            .then(response => response.json())
            .then(data => {
                if (typeof data.doctor_account == 'undefined') {
                    M.toast({ html: 'Doctor no registrado en la base de datos!' });
                } else if (doctor_id == data.doctor_account.doctor_id && doctor_password == data.doctor_account.doctor_password) {
                    location.href = '/doctor/' + doctor_id;
                }
                else {
                    M.toast({ html: 'Error en usuario o contrasena!' });
                }
            });
    }
}

// Doctor Form fields

let d_id = d.getElementById("d_id");

let d_name = d.getElementById("d_name");

let d_sname = d.getElementById("d_sname");

let d_lastname = d.getElementById("d_lastname");

let d_slastname = d.getElementById("d_slastname");

let d_bdate = d.getElementById("d_bdate");


// Update patient data

function update_doctor() {

    let u_id_value = parseInt(d_id.value);
    let u_name_value = d_name.value;
    let u_sname_value = d_sname.value;
    let u_lastname_value = d_lastname.value;
    let u_slastname_value = d_slastname.value;
    let u_bdate_value = d_bdate.value;
    
    if (u_id_value == '') {
        M.toast({ html: 'Campo de cedula vacio!' });
    } if (u_name_value == '') {
        M.toast({ html: 'Campo de nombre vacio!' });
    } if (u_sname_value == '') {
        M.toast({ html: 'Campo de s_nombre vacio!' });
    } if (u_lastname_value == '') {
        M.toast({ html: 'Campo de apellido vacio!' });
    } if (u_slastname_value == '') {
        M.toast({ html: 'Campo de s_apellido vacio!' });
    } if (u_bdate_value == '') {
        M.toast({ html: 'Campo de f_nacimiento vacio!' });
    } if (u_id_value != '' && u_name_value != '' && u_sname_value != '' && u_lastname_value != '' && u_slastname_value != '' && u_bdate_value != '') {

        fetch('http://localhost:8000/api/persons/'+u_id_value, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                person_id: u_id_value,
                name: u_name_value,
                second_name: u_sname_value,
                lastname: u_lastname_value,
                second_lastname: u_slastname_value,
                age: u_bdate_value,
                
            }),
        })
            .then(response => {
                
                
                M.toast({html: 'Datos Actualizados!'});

                alert('Datos Actualizados!');

                location.href = '/doctor/' + u_id_value;

            })

    }
}

// User Form fields

let u_id = d.getElementById("u_id");

let u_name = d.getElementById("u_name");

let u_sname = d.getElementById("u_sname");

let u_lastname = d.getElementById("u_lastname");

let u_slastname = d.getElementById("u_slastname");

let u_bdate = d.getElementById("u_bdate");

// Update patient data



function update_user() {

    let u_id_value = parseInt(u_id.value);
    let u_name_value = u_name.value;
    let u_sname_value = u_sname.value;
    let u_lastname_value = u_lastname.value;
    let u_slastname_value = u_slastname.value;
    let u_bdate_value = u_bdate.value;
    
    if (u_id_value == '') {
        M.toast({ html: 'Campo de cedula vacio!' });
    } if (u_name_value == '') {
        M.toast({ html: 'Campo de nombre vacio!' });
    } if (u_sname_value == '') {
        M.toast({ html: 'Campo de s_nombre vacio!' });
    } if (u_lastname_value == '') {
        M.toast({ html: 'Campo de apellido vacio!' });
    } if (u_slastname_value == '') {
        M.toast({ html: 'Campo de s_apellido vacio!' });
    } if (u_bdate_value == '') {
        M.toast({ html: 'Campo de f_nacimiento vacio!' });
    } if (u_id_value != '' && u_name_value != '' && u_sname_value != '' && u_lastname_value != '' && u_slastname_value != '' && u_bdate_value != '') {

        fetch('http://localhost:8000/api/persons/'+u_id_value, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                person_id: u_id_value,
                name: u_name_value,
                second_name: u_sname_value,
                lastname: u_lastname_value,
                second_lastname: u_slastname_value,
                age: u_bdate_value,
                
            }),
        })
            .then(response => {

                M.toast({html: 'Datos Actualizados!'});

                alert('Datos Actualizados!');

                location.href = '/user/' + u_id_value;

            })

    }
}

function go_doctor(id) {
    location.href = '/doctor/' + id;
}

function go_user(id) {
    location.href = '/user/' + id;
}


// Patient List
const renderPost = (posts) => {
    posts.forEach((post) => {
        output += `
          <div class="card mt-4 col-md-6 bg-ligt ">
            <img src=${post.url} class="" alt="" width="100%" 
            height="400"">
            <div class="card-body" data-id=${post.id}>
              <h5 class="card-title name">${post.name}</h5>
              <h6 class="card-subtitle mb-2 text-muted price">${post.price}</h6>
              <p class="card-title desc">${post.description}</p>
              <p class="card-title url">${post.url}</p>
              <a href="#" class="btn btn-primary" id="edit-post">Editar</a>
              <a href="#" class="btn btn-primary" id="delete-post">Eliminar</a>
            </div>
          </div>
  `;
    });
    $postList.innerHTML = output;
};

fetch(url)
    .then((res) => res.json())
    .then((data) => renderPost(data));

// User Register Form

let ru_id = d.getElementById("ru_id");

let ru_name = d.getElementById("ru_name");

let ru_sname = d.getElementById("ru_sname");

let ru_lastname = d.getElementById("ru_lastname");

let ru_slastname = d.getElementById("ru_slastname");

let ru_bdate = d.getElementById("ru_bdate");

// Update patient data



function register_user() {

    let u_id_value = parseInt(ru_id.value);
    let u_name_value = ru_name.value;
    let u_sname_value = ru_sname.value;
    let u_lastname_value = ru_lastname.value;
    let u_slastname_value = ru_slastname.value;
    let u_bdate_value = ru_bdate.value;

    if (u_id_value == '') {
        M.toast({ html: 'Campo de cedula vacio!' });
    } if (u_name_value == '') {
        M.toast({ html: 'Campo de nombre vacio!' });
    } if (u_sname_value == '') {
        M.toast({ html: 'Campo de s_nombre vacio!' });
    } if (u_lastname_value == '') {
        M.toast({ html: 'Campo de apellido vacio!' });
    } if (u_slastname_value == '') {
        M.toast({ html: 'Campo de s_apellido vacio!' });
    } if (u_bdate_value == '') {
        M.toast({ html: 'Campo de f_nacimiento vacio!' });
    } if (u_id_value != '' && u_name_value != '' && u_sname_value != '' && u_lastname_value != '' && u_slastname_value != '' && u_bdate_value != '') {

        fetch('http://localhost:8000/api/persons/'+u_id_value, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                person_id: u_id_value,
                name: u_name_value,
                second_name: u_sname_value,
                lastname: u_lastname_value,
                second_lastname: u_slastname_value,
                age: u_bdate_value,

            }),
        })
            .then(response => {

                fetch('http://localhost:8000/api/patient/'+u_id_value, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                person_id: u_id_value,
                patient_id: u_name_value,


            }),
        })

                fetch('http://localhost:8000/api/user_accounts/'+u_id_value, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                user_account_id: 12328,
			patient_id: 12328,
			user_email: "12328@gmail.com",
			user_password: "qwe123",
			username:


            }),
        })


                location.href = '/user_created/' + u_id_value;

            })

    }
}
