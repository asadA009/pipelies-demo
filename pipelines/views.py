from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyze(request):
    djtext= request.GET.get('text','defualt')
    removepunc= request.GET.get('removepunc','off')
    print(djtext)
    print(removepunc)

    if removepunc=='off':
        punctions=''' !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ '''
        analyze=""
        for char in djtext:
            if char not in punctions:
                analyze=analyze + char
        params={'purpose':'Remove punctions','analyzed_text':analyze}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse('Error')