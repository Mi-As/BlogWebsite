from django.shortcuts import render
from django.views import generic
from .models import Page

class DefaultPage(generic.DetailView):
    model = Page
    template_name = 'page/default_page.html'
