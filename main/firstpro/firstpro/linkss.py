from django.http import HttpResponse
from django.shortcuts import render
from textblob import TextBlob
def func1(request):
    return render(request,"func1.html")

def func2(request):

    djtext = request.GET.get('text', 'default')

    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    spell_check = request.GET.get('spell_check', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = { 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = { 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed=analyzed+char
        params = {'analyzed_text': analyzed}

        djtext=analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params ={ 'analyzed_text': analyzed}
        djtext = analyzed

    if spell_check=="on":
        analyze=TextBlob(djtext)
        analyzed=analyze.correct()
        params={'analyzed_text':analyzed}
        djtext = analyzed




    l={"removepunc":removepunc,"fullcaps":fullcaps,"newlineremover":newlineremover,"extraspaceremover":extraspaceremover,"spell_check":spell_check}
    add=""
    for i,j in l.items():
        if j=="on":
            add+=(i+",")
    params["purpose"]=add

    return render(request, 'func2.html', params)

def func3(request):
    return HttpResponse("Input your text, check your desired button and get the corresponding output")
def func4(request):
    return HttpResponse("Absolutely Free")
def blogR(request):
    return render(request,"blog.html")
def spellcheck(data):
    analyze = TextBlob(data)
    analyzed = analyze.correct()
    return analyzed


