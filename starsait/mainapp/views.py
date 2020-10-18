from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html')


def evidence(request):
    return render(request, 'mainapp/evidence.html')


def list(request):
    return render(request, 'mainapp/list.html')


def description(request):
    return render(request, 'mainapp/description.html')