from django.shortcuts import render

from django.views.generic.list import ListView

from .models import MyObject

# Create your views here.
class IndexView(ListView):
    model = MyObject
    context_object_name = 'objects'
    template_name = 'first_app/index.html'