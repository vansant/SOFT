# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import zipfile
from json import dumps

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

import shapefile

def unzip_folder(zipped_file, output_path=""):
    """ Unzips folder to a directory
        zipped_file:			
        	Path to the folder to unzip
        out_put:
    	    Path to unzip folder to.
    """
    output_path = r"{}".format(output_path)
    zipped_files = zipfile.ZipFile(zipped_file, 'r')
    zipped_files.extractall(output_path+zipped_file[:-4])
    zipped_files.close()

    return zipped_file[:-4]

def shapefile_to_GeoJSON(path_to_shapefile):
	""" Takes a shapefile and converts it to GeoJSON"""
    
    # Open shapfile reader
    shapefile_reader = shapefile.Reader(path_to_shapefile)

    # Get shapefile field information
    fields = shapefile_reader.fields[1:]
    field_names = [field_name[0] for field_name in fields]

    # List to hold features
    features = []

    # Get shapefile record and geometry data
    for shapefile_record in shapefile_reader.shapeRecords():
        attribute = dict(zip(field_names, shapefile_record.record))
        shapefile_record_geometry = shapefile_record.shape.__geo_interface__
        features.append(dict(type="Feature", geometry=shapefile_record_geometry, properties=attribute)) 

    # Write the GeoJSON file
    geojson = open("static/shapefiles/{}.geojson".format(os.path.split(path_to_shapefile)[-1][:-4]), "w")
    geojson.write(dumps({"type": "FeatureCollection", "features": features}))
    geojson.close()

def handle_uploaded_file(zipped_folder):
	""" Manages what happens to uploaded files"""
    zipped_folder_name = str(zipped_folder)
    with open(r'static/shapefiles/{}'.format(zipped_folder), 'wb+') as destination:
        for chunk in zipped_folder.chunks():
            destination.write(chunk)
    unzipped_shapefile_folder = unzip_folder(r'static/shapefiles/{}'.format(zipped_folder))
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    shapefile_path = os.path.join(os.path.dirname(BASE_DIR), 'SOFT', "static", "shapefiles", "{}".format((zipped_folder_name[:-4])), "{}".format((zipped_folder_name[:-4])), "{}".format((zipped_folder_name[:-4])) +".shp")
    shapefile_to_GeoJSON(r'{}'.format(shapefile_path))



def upload_file(request):
	""" View to upload files with"""
    if request.method == 'POST':
    	handle_uploaded_file(request.FILES['file'])
        return render(request, 'shapefile2GeoJSON/index.html', {
           'site_title': 'posted',
        })
    else:
        pass


def index(request):
    # View code here...
    return render(request, 'shapefile2GeoJSON/index.html', {
        'site_title': 'shapefile2GeoJSON',
    })
