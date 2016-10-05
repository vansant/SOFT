# SOFT
Style on the Fly 

# Local Use
## This Django powered app is intended for local use in a web browser to generate a static HTTP webmap. If you want to modify it for a production use make sure you know what you are doing - the secret keep was intentionally left simple. A better way to do this would be to load in a secret key from a system environment variable to keep the secret key out of the source code.

# Install required Python Modules
## $./pip install requirements.txt

# Run tests from root directory
## $./python tests.py

#To Do List

##Python webserver - handle http and work with zipped files, GeoJSON and shapefiles
##Shapefile upload page - drag zipped shapefile into webbrowser or upload by selecting zipped shapefile - convert to GeoJSON with Python code on backend
##Send GeoJSON to Leaflet webmap
##Setup GeoJSON Styles - on the fly style option with the ability to generate a simple website
##Write Tests
##Refactor Code

