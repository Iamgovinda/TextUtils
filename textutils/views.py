#made by myself#made by myself
#made by myself

import http
from sqlite3 import paramstyle
from string import punctuation
import django
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'name':'govinda','place':'mars'}
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')

    #checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')

    #check for removepunc
    if removepunc=='on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
            print(char)
        params= {'purpose':'Removed Punctuations','analyzed_text': analyzed}
        #analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    #check for fullcaps
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params= {'purpose':'Removed New Lines','analyzed_text': analyzed}
        djtext = analyzed

    #check for newlineremover
    if newlineremove == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params= {'purpose':'Changed to Newlineremoving','analyzed_text': analyzed}
        djtext = analyzed

    #check for spaceremover

    if extraspaceremove == 'on':
        analyzed=""

        for index, char in enumerate(djtext):
            if not index == len(djtext)-1:
                if not djtext[index]==" " or djtext[index+1]== " ":
                    analyzed = analyzed + char
            

        params= {'purpose':'Changed to Extra space removing','analyzed_text': analyzed}
        djtext = analyzed

    if removepunc=='off' and extraspaceremove == 'off' and newlineremove == 'off' and fullcaps == 'off':
        return render(request, "index.html")

    return render(request,"analyze.html",params)


def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
# 


