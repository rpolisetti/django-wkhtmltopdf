from django.shortcuts import render
from django.views.generic import TemplateView
from wkhtmltopdf.views import PDFTemplateView
from weasyprint import HTML,CSS
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = "about.html"