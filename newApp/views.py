# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader


def index(request):
    return render(request, template_name='index.html', context={})
