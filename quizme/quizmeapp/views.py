from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
	return render(request, 'index.html', {})

def quizcreation(request):
	return render(request, 'quiz-creation.html', {})
