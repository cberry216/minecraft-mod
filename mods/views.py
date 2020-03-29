from django.shortcuts import render

from .models import Mod

# Create your views here.


def index(request):
    mods = Mod.objects.all()

    return render(request, 'mods/index.html', {
        'mods': mods
    })
