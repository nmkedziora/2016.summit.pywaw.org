from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^code-of-conduct/$', TemplateView.as_view(template_name='code_of_conduct.html'), name='code-of-conduct'),
]
