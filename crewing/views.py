from django.shortcuts import render, redirect

from .models import Seamans
from .forms import SeamanForm


def seamans_list(request):
    seamans = Seamans.objects.all()
    return render(request, 'crewing/seamans_list.html', {'seamans': seamans})


def seamancard(request):
    return render(request, 'crewing/seamancard.html')


def seaman_add(request):
    form = SeamanForm()
    if request.method == 'POST':
        form = SeamanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seamans_list')
        else:
            return render(request, 'crewing/seaman.html', {'form': form, })
    else:
        return render(request, 'crewing/seaman.html', {'form': form})
