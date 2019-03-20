from django.shortcuts import render, redirect, get_object_or_404

from .models import Seamans, Ranks, Vessels, Contracts, Opinions
from .forms import SeamanForm, RankForm


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


def rank_list(request):
    title = 'Справочник должностей'
    ranks = Ranks.objects.all()
    return render(request, 'crewing/rank_list.html',
                  {'ranks': ranks, 'title': title})


def rank_add(request):
    title = 'Добавить должность'
    form = RankForm()
    if request.method == 'POST':
        form = RankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rank_list')
        else:
            return render(request, 'crewing/rank.html',
                   {'title': title, 'form': form})
    else:
        return render(request, 'crewing/rank.html',
                      {'title': title, 'form': form})


def rank_edit(request, rank_id):
    title = 'Редактировать должность'
    rank = get_object_or_404(Ranks, id=rank_id)
    if request.method == 'POST':
        form = RankForm(request.POST, instance=rank)
        if form.is_valid():
            form.save()
            return redirect('rank_list')
        else:
            return render(request, 'crewing/rank.html',
                   {'title': title, 'form': form, 'rank': rank})
    else:
        form = RankForm(instance=rank)
        return render(request, 'crewing/rank.html',
                      {'title': title, 'form': form, 'rank': rank})
