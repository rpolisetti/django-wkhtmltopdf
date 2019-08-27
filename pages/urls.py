# pages/urls.py
from django.urls import path

from .views import HomePageView, AboutPageView
from wkhtmltopdf.views import PDFTemplateView 


urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('pdf/', PDFTemplateView.as_view(template_name='firefox.html',
                                        filename='my_pdf.pdf',
                                        cmd_options = {
                                                       'page-size': 'A4',
                                                       'encoding': "UTF-8",
                                                        'print-media-type': '',
                                                        'page-size': 'A4',
                                                        'margin-top': '10mm',
                                                        'margin-bottom': '10mm',
                                                        'margin-left': '10mm',
                                                        'margin-right': '10mm',
                                                        'zoom': '1.50',
                                                    },
                                        show_content_in_browser = True)
                                        , name='pdf'),
    path('about/', AboutPageView.as_view(), name='about'),
]