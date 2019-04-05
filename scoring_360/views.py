from django.shortcuts import render


# заглушка
def test(request):
    return render(request, 'scoring_360/test.html')
