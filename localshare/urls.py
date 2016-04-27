from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'createsharable', views.sharable, name='sharable'),
    url(r'Utoo/(?P<route>[^/]+)', views.finaldisplay, name='finaldisplay'),
]
