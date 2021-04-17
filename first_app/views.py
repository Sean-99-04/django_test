from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from .models import MyObject

# Create your views here.
class IndexView(ListView):
    model = MyObject
    context_object_name = 'objects'
    template_name = 'first_app/index.html'

class ObjectCreate(CreateView):
    model = MyObject
    fields = ['title', 'description']
    template_name = 'first_app/form.html'
    success_url = reverse_lazy('index')
    # form_class = MyObject