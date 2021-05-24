from django.http import HttpResponse
from django.shortcuts import render


def front(request): 
  return HttpResponse(render(request, 'vue_index.html'))




