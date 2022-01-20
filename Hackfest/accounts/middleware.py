from urllib import response
from django.shortcuts import redirect


def auth_middleware(get_response):
    def Admin(request):
        if request.session.get("role") != "Admin":  

            return redirect('/accounts/loginpage')
   
        response = get_response(request)
        return response
    return Admin


def check_middleware(get_response):
    def Admin(request,roledata):
        if request.session.get("role") != "Admin":  

            return redirect('/accounts/loginpage')
   
        response = get_response(request, roledata)
        return response
    return Admin
    


def doctor_middleware(get_response):
    def doctor(request):
        if request.session.get("role") != "Doctor":  
            return redirect('/accounts/loginpage')
   
        response = get_response(request)
        return response
    return doctor
def doctordata_middleware(get_response):
    def doctor(request, newdata):
        if request.session.get("role") != "Doctor":  
            return redirect('/accounts/loginpage')
   
        response = get_response(request, newdata)
        return response
    return doctor

def both_middleware(get_response):
    def both(request):
        if request.session.get("role") !=  "Doctor" and request.session.get("role") !="Nurse":
            return redirect('/accounts/loginpage')
        response = get_response(request)
        return response
    return both

def bothdata_middleware(get_response):
    def both(request, roledata):
        if request.session.get("role") !=  "Doctor" and request.session.get("role") !="Nurse":
            return redirect('/accounts/loginpage')
        response = get_response(request, roledata)
        return response
    return both





def nurse_middleware(get_response):
    def nurse(request):
        if request.session.get("role") !="Nurse":
            return redirect('/accounts/loginpage')
        response = get_response(request)
        return response
    return nurse

 
def nursedata_middleware(get_response):
    def nurse(request, roledata):
        if request.session.get("role") !="Nurse":
            return redirect('/accounts/loginpage')
        response = get_response(request, roledata)
        return response
    return nurse
 