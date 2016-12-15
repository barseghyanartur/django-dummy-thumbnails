wget -O django_dummy_thumbnails_demo_installer.tar.gz https://github.com/barseghyanartur/django-dummy-thumbnails/archive/stable.tar.gz
virtualenv django-dummy-thumbnails
source django-dummy-thumbnails/bin/activate
mkdir django_dummy_thumbnails_demo_installer/
tar -xvf django_dummy_thumbnails_demo_installer.tar.gz -C django_dummy_thumbnails_demo_installer
cd django_dummy_thumbnails_demo_installer/django-dummy-thumbnails-stable/examples/simple/
pip install -r ../../requirements.txt
pip install https://github.com/barseghyanartur/django-dummy-thumbnails/archive/stable.tar.gz
mkdir ../media/
mkdir ../media/static/
mkdir ../static/
mkdir ../db/
mkdir ../logs/
mkdir ../tmp/
cp settings/local_settings.example settings/local_settings.py
./manage.py migrate --noinput --traceback -v 3
./manage.py collectstatic --noinput --traceback -v 3
./manage.py dummy_thumbnails_symlink_dummy_images
./manage.py runserver 0.0.0.0:8001 --traceback -v 3
