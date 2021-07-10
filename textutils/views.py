from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char
        djtext = analyzed
        params = {'value': analyzed}

    if uppercase == 'on':
        analyzed = ''
        for char in djtext:
            analyzed=analyzed+char.upper()
        djtext = analyzed
        params = {'value': analyzed}

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char!='\n' and char !='\r':
                analyzed = analyzed + char
        djtext = analyzed
        params = {'value': analyzed}

    if extraspaceremover == 'on':
        analyzed = ''
        for index,char in enumerate (djtext):

            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        djtext = analyzed
        params = {'value': analyzed}

    if charcount == 'on':
        analyzed =0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'value': analyzed}

    elif removepunc != 'on'and uppercase == 'on' and newlineremover == 'on' and extraspaceremover == 'on' and charcount == 'on':
        return HttpResponse('Please enter any character')

    return render(request, 'analyze.html', params)
