#from django.test import TestCase

# Create your tests here.

if request.method == 'POST':
        uid = request.POST['person_id']
        if (uid != 0):
            uacount = list(Person.objects.filter(person_id=uid).values())
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

                return redirect('/user/'+str(id))

            else:
                return redirect(request.META.get('HTTP_REFERER'))
                msg = "Parece que los datos ingresados son incorrectos"
        else:
            msg = "Parece que los datos ingresados"
