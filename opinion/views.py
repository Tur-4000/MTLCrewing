from django.shortcuts import render, get_object_or_404, redirect

from crewing.models import Seamans, Contracts
from .forms import OpinionForm
from .models import Opinion


def opinion_add(request, seaman_id):
    title = 'Добавить отзыв'
    seaman = get_object_or_404(Seamans, id=seaman_id)
    qs = Contracts.objects.filter(seaman=seaman_id).all()

    if request.method == 'POST':
        form = OpinionForm(request.POST, request.FILES, contracts=qs)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.seaman = seaman
            obj.save()
            return redirect('seamancard', seaman_id)
    else:
        form = OpinionForm(contracts=qs)

    context = {'title': title, 'form': form, 'seaman': seaman}
    return render(request, 'opinion/opinion.html', context)


def opinion_edit(request, seaman_id, opinion_id):
    title = 'Редактировать отзыв'
    seaman = get_object_or_404(Opinion, id=seaman_id)
    opinion = get_object_or_404(Opinion, id=opinion_id)
    qs = Contracts.objects.filter(seaman=seaman_id).all()

    if request.method == 'POST':
        form = OpinionForm(request.POST, request.FILES, instance=opinion, contracts=qs)
        if form.is_valid():
            form.save()
            return redirect('seamancard', seaman.id)
    else:
        form = OpinionForm(instance=opinion, contracts=qs)

    context = {'title': title, 'form': form,
               'opinion': opinion, 'seaman': seaman}
    return render(request, 'opinion/opinion.html', context)
