from django.http import HttpResponse
from django.shortcuts import render


def home(Request):
    return render(Request, 'home.html')


def about(Request):
    return render(Request, 'about.html')
    

def count(Request):
    fulltext = Request.GET['fulltext']
    wordlist = fulltext.split()
    return render(Request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist)})
