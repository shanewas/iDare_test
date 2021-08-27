from django.shortcuts import render


def home(request):
    return render(request, 'tasks/home.html')


def status(request):
    return render(request, 'tasks/status.html', {'title': 'Status'})
