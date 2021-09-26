# from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "index.html"