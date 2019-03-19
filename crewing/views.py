from django.shortcuts import render, redirect, get_object_or_404

from .models import Seamans
from .forms import SeamanForm


def seamans_list(request):
    seamans = Seamans.objects.all()
    return render(request, 'crewing/seamans_list.html', {'seamans': seamans})


def seamancard(request, seaman_id):
    seaman = get_object_or_404(Seamans, id=seaman_id)
    return render(request, 'crewing/seamancard.html', {'seaman': seaman})


def seaman_add(request):
    title = 'Добавить моряка'
    form = SeamanForm()
    if request.method == 'POST':
        form = SeamanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seamans_list')
        else:
            return render(request, 'crewing/seaman.html',
                          {'form': form, 'title': title})
    else:
        return render(request, 'crewing/seaman.html',
                      {'form': form, 'title': title})


def seaman_edit(request, seaman_id):
    title = 'Редактировать моряка'
    seaman = get_object_or_404(Seamans, id=seaman_id)
    if request.method == 'POST':
        form = SeamanForm(request.POST, instance=seaman)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'crewing/seaman.html',
                          {'form': form, 'seaman': seaman, 'title': title})
        return redirect('seamans_list')
    else:
        form = SeamanForm(instance=seaman)
        return render(request, 'crewing/seaman.html',
                      {'form': form, 'seaman': seaman, 'title': title})
