# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    # View code here...
    return render(request, 'shapefile2GeoJSON/index.html', {
        'site_title': 'shapefile2GeoJSON',
    })
