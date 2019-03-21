from django.shortcuts import render, redirect, get_object_or_404

from .models import Seamans, Ranks, Vessels, Contracts, Opinions
from .forms import SeamanForm, RankForm, VesselForm, OpinionForm, ContractForm


def seamans_list(request):
    seamans = Seamans.objects.all()
    return render(request, 'crewing/seamans_list.html', {'seamans': seamans})


def seamancard(request, seaman_id):
    seaman = get_object_or_404(Seamans, id=seaman_id)
    contracts = Contracts.objects.filter(seaman=seaman_id).all()
    opinions = Opinions.objects.filter(seaman=seaman_id).all()
    return render(request, 'crewing/seamancard.html',
                  {'seaman': seaman, 'contracts': contracts, 'opinions': opinions})


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


def vessels_list(request):
    title = 'Справочник судов'
    vessels = Vessels.objects.all()
    return render(request, 'crewing/vessels_list.html',
                  {'title': title, 'vessels': vessels})


def vessel_add(request):
    title = 'Добавить судно'
    if request.method == 'POST':
        form = VesselForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vessels_list')
        else:
            return render(request, 'crewing/vessel.html',
                          {'title': title, 'form': form})
    else:
        form = VesselForm()
        return render(request, 'crewing/vessel.html',
                      {'title': title, 'form': form})


def vessel_edit(request, vessel_id):
    title = 'Редактировать судно'
    vessel = get_object_or_404(Vessels, id=vessel_id)
    if request.method == 'POST':
        form = VesselForm(request.POST, instance=vessel)
        if form.is_valid():
            form.save()
            return redirect('vessels_list')
        else:
            return render(request, 'crewing/vessel.html',
                          {'title': title, 'form': form, 'vessel': vessel})
    else:
        form = VesselForm(instance=vessel)
        return render(request, 'crewing/vessel.html',
                      {'title': title, 'form': form, 'vessel': vessel})


def opinion_add(request, seaman_id):
    title = 'Добавить отзыв'
    seaman = get_object_or_404(Seamans, id=seaman_id)
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.seaman = seaman
            obj.save()
            return redirect('seamancard', seaman_id)
        else:
            return render(request, 'crewing/opinion.html',
                          {'title': title, 'form': form, 'seaman': seaman})
    else:
        form = OpinionForm()
        return render(request, 'crewing/opinion.html',
                      {'title': title, 'form': form, 'seaman': seaman})


def contract_add(request, seaman_id):
    title = 'Добавить контракт'
    seaman = get_object_or_404(Seamans, id=seaman_id)
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.seaman = seaman
            obj.save()
            return redirect('seamancard', seaman_id)
        else:
            return render(request, 'crewing/contract.html',
                  {'title': title, 'form': form, 'seaman': seaman})
    else:
        form = ContractForm()
        return render(request, 'crewing/contract.html',
                      {'title': title, 'form': form, 'seaman': seaman})
