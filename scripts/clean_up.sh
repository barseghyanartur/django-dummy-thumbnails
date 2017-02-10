find . -name "*.pyc" -exec rm -rf {} \;
find . -name "__pycache__" -exec rm -rf {} \;
find . -name "*.orig" -exec rm -rf {} \;
rm -rf build/
rm -rf dist/
rm -rf src/django_dummy_thumbnails.egg-info
rm -rf src/django-dummy-thumbnails.egg-info
rm -rf .cache/
