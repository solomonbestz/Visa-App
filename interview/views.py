from django.shortcuts import render

# Create your views here.
def interview(request):
    return render(request, 'interview/interview.html')