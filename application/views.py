from django.shortcuts import render, redirect
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

        apply = Application.objects.create(passport_number = passport_number,
                                        passport_photo= passport_photo,
                                        application_country= application_country,
                                        nigeria_embassy =nigeria_embassy,
                                        date_of_birth = dob,
                                        email =email,
                                        date_of_entry = doe,
                                        visa_type =visa_type)
        apply.save()
        send_message("Application Successful", message, email)
        return redirect('home')


    return render(request, 'application/application.html')
