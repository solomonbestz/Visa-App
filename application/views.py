from django.shortcuts import render
from .email import send_message
from .models import *

# Create your views here.
def application(request):
    message: str = 'Your application was succesful and your interview scheduled, check interview section to know your date for the interview.'
    if request.method == 'POST':
        passport_number = request.POST.get('pass_num')
        passport_photo = request.POST.get("pass_photo")
        application_country = request.POST.get("app_country")
        nigeria_embassy = request.POST.get("embassy")
        dob = request.POST.get("date_birth")
        email = request.POST.get("email")
        doe = request.POST.get("date_entry")
        visa_type = request.POST.get("visa_type")

    apply = Application.objects.create(passport_number,
                                       passport_photo,
                                       application_country,
                                       nigeria_embassy,
                                       dob,
                                       email,
                                       doe,
                                       visa_type)
    apply.save()
    send_message("Application Successful", message, email)


    return render(request, 'application/application.html')
