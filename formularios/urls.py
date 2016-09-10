from django.conf.urls import url
from django.contrib import admin
from core.views import form_manual, django_form


urlpatterns = [
    url(r'^$', form_manual, name='core_form_manual'),	
    url(r'^django-form/$', django_form, name='core_form_django'),	
    url(r'^admin/', admin.site.urls),
]
