from django.shortcuts import render
from .tasks import my_task


def home(request):
    return render(request, 'tasks/home.html')


async def status(request):
    my_task.delay()
    return render(request, 'tasks/status.html', {'title': 'Status'})

