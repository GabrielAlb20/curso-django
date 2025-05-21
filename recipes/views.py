from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse('''<!DOCTYPE
    <html>
    <head><title>Olá mundo</title></head>
    
    
    <body>
        <h1>Olá Mundo</h1>
    </body>
    
    <html>       
    ''')

def contato(request):
    return HttpResponse('CONTATO')

def sobre(request):
    return HttpResponse('SOBRE')