from django.shortcuts import render, redirect, get_object_or_404

from .models import Seamans, Ranks, Vessels, Contracts
from opinion.models import Opinion
from scoring_360.models import Question360
from .forms import SeamanForm, RankForm, VesselForm, ContractForm
from .utils import last_rank




def seamans_list(request):
    seamans = Seamans.objects.all()
    context = {'seamans': seamans}
    return render(request, 'crewing/seamans_list.html', context)


def seamancard(request, seaman_id):
    seaman = get_object_or_404(Seamans, id=seaman_id)
    contracts = Contracts.objects.filter(seaman=seaman_id).all()
    opinions = Opinion.objects.filter(seaman=seaman_id).all()

    context = {'seaman': seaman, 'contracts': contracts,
               'opinions': opinions}

    if seaman.last_rank:
        rank = get_object_or_404(Ranks, id=seaman.last_rank.id)
        obj = Question360.objects.filter(ranks=rank).prefetch_related('ability')
        ability = []
        for item in obj:
            ability.append(item.ability)
        abilities = set(ability)
        # abilities = rank.abilities.all()
        context['abilities'] = abilities

    return render(request, 'crewing/seamancard.html', context)


def seaman_add(request):
    title = 'Добавить моряка'

    if request.method == 'POST':
        form = SeamanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seamans_list')
    else:
        form = SeamanForm()

    context = {'form': form, 'title': title}
    return render(request, 'crewing/seaman.html', context)


def seaman_edit(request, seaman_id):
    title = 'Редактировать моряка'
    seaman = get_object_or_404(Seamans, id=seaman_id)

    if request.method == 'POST':
        form = SeamanForm(request.POST, request.FILES, instance=seaman)
        if form.is_valid():
            form.save()
            return redirect('seamans_list')
    else:
        form = SeamanForm(instance=seaman)

    context = {'form': form, 'seaman': seaman, 'title': title}
    return render(request, 'crewing/seaman.html', context)


def rank_list(request):
    title = 'Справочник должностей'
    ranks = Ranks.objects.all()
    context = {'ranks': ranks, 'title': title}
    return render(request, 'crewing/rank_list.html', context)


def rank_add(request):
    title = 'Добавить должность'

    if request.method == 'POST':
        form = RankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rank_list')
    else:
        form = RankForm()

    context = {'title': title, 'form': form}
    return render(request, 'crewing/rank.html', context)


def rank_edit(request, rank_id):
    title = 'Редактировать должность'
    rank = get_object_or_404(Ranks, id=rank_id)

    if request.method == 'POST':
        form = RankForm(request.POST, instance=rank)
        if form.is_valid():
            form.save()
            return redirect('rank_list')
    else:
        form = RankForm(instance=rank)
    context = {'title': title, 'form': form, 'rank': rank}

    return render(request, 'crewing/rank.html', context)


def vessels_list(request):
    title = 'Справочник судов'
    vessels = Vessels.objects.all()
    context = {'title': title, 'vessels': vessels}
    return render(request, 'crewing/vessels_list.html', context)


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

    context = {'title': title, 'form': form}
    return render(request, 'crewing/vessel.html', context)


def vessel_edit(request, vessel_id):
    title = 'Редактировать судно'
    vessel = get_object_or_404(Vessels, id=vessel_id)

    if request.method == 'POST':
        form = VesselForm(request.POST, instance=vessel)
        if form.is_valid():
            form.save()
            return redirect('vessels_list')
    else:
        form = VesselForm(instance=vessel)

    context = {'title': title, 'form': form, 'vessel': vessel}
    return render(request, 'crewing/vessel.html', context)


def contract_add(request, seaman_id):
    title = 'Добавить контракт'
    seaman = get_object_or_404(Seamans, id=seaman_id)

    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.seaman = seaman
            obj.save()
            seaman.last_rank = last_rank(seaman_id)
            seaman.save()
            return redirect('seamancard', seaman_id)
    else:
        form = ContractForm()

    context = {'title': title, 'form': form, 'seaman': seaman}
    return render(request, 'crewing/contract.html', context)


def contract_edit(request, seaman_id, contract_id):
    title = 'Редактировать контракт'
    contract = get_object_or_404(Contracts, id=contract_id)
    seaman = get_object_or_404(Seamans, id=seaman_id)

    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.seaman = seaman
            obj.save()
            seaman.last_rank = last_rank(seaman_id)
            seaman.save()
            return redirect('seamancard', seaman_id)
    else:
        form = ContractForm(instance=contract)

    context = {'title': title, 'form': form, 'seaman': seaman}
    return render(request, 'crewing/contract.html', context)
