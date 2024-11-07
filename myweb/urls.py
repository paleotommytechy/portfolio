from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.homepage, name='home'),
    path('about/',views.about, name='about'),
    path('projects/',views.project, name='projects'),
    path('testimonies/',views.testimonies, name='testimonies'),
    path('contact/',views.contact, name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)