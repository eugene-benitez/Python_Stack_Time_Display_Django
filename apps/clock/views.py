from django.shortcuts import render
from time import gmtime, strftime


def index(request):
    context = {
        "time": strftime("%b %m, %d %H:%M %p", gmtime())
    }
    return render(request, 'clock/index.html', context)
