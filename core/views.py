from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = 'core/index.html'
