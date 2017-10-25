from django.conf.urls import include, url
from .views import InicioView
urlpatterns = [
    url(r'^$', InicioView.as_view(), name='inicio'),

]
