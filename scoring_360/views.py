from django.shortcuts import render, redirect, get_object_or_404

from .forms import Question360Form
from .models import Question360


# заглушка
def test(request):
    return render(request, 'scoring_360/test.html')


def questions360_list(request):
    title = 'Вопросы рейтинга 360 (моряки)'
    questions = Question360.objects.all()
    context = {'title': title, 'questions': questions}
    return render(request, 'scoring_360/questions360_list.html', context)


def question360_add(request):
    title = 'Добавить вопрос рейтинга 360 (моряки)'

    if request.method == 'POST':
        form = Question360Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scoring_360:questions360_list')
    else:
        form = Question360Form()

    context = {'title': title, 'form': form}
    return render(request, 'scoring_360/question.html', context)


def question360_edit(request, question_id):
    title = 'Редактировать вопрос рейтинга 360 (моряки)'
    question = get_object_or_404(Question360, id=question_id)
    if request.method == 'POST':
        form = Question360Form(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('scoring_360:questions360_list')
    else:
        form = Question360Form(instance=question)

    context = {'title': title, 'form': form}
    return render(request, 'scoring_360/question.html', context)
