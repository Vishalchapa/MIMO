from django.views.generic import TemplateView
from django.shortcuts import render

class IndexPage(TemplateView):
    template_name = 'core/index.html'

def about(request):
    return render(request, 'core/about.html')

def how_to_use(request):
    return render(request, 'core/how_to_use.html')
