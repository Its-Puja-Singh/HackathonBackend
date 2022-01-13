from django.shortcuts import render, HttpResponse, redirect
import datetime
import random
from healthcare.models import Patient
import uuid
# Create your views here.
def newPatient(request):
    # if request.user.is_authenticated:
        if request.session['user_type'] == 'Receptionist':
            if request.method == 'POST':
                name = request.POST['name']
                mobile = request.POST['mobile']
                email = request.POST['email']
                gender = request.POST['gender']
                age = request.POST['age']
                height = request.POST['height']
                bloodGroup = request.POST['blood_group']
                uuidNo = str(uuid.uuid4()).replace("-","")[0:10]
                registrationNumber = name.replace(' ','')+uuidNo+str(random.randint(2345678909800, 9923456789000))[0:5]
                patientData = Patient(name,mobile,email,gender,age,height,bloodGroup,registrationNumber)
                patientData.save()
                return redirect('/healthcare/newPatient', patientData)
            else:
                return render(request, '/healthcare/newPatient')

        else:
            return redirect('/')
    # else:
    #         return redirect('/')
