from django.http import JsonResponse
from django.shortcuts import render

def home_page(request):
    word = request.GET.get('word')
    if word:
        context = {
            'word': 'Hi ' + word,
        }
        return JsonResponse(context)
    else:
        return render(request, 'home_page.html')
