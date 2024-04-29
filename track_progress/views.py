from django.shortcuts import render

# Create your views here.
def track(request):
    return render(request, 'track_progress/track.html')