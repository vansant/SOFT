from django.conf.urls import url

from . import views

app_name = 'shapefile2GeoJSON'
urlpatterns = [
    url(r'^$', views.index, name='index'),

]