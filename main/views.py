from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from models import SimpleUser


class MainPageView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = SimpleUser.objects.all()

        return context
