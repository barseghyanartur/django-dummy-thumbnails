reset
./scripts/uninstall.sh
#./scripts/install_django_1_8.sh
#python examples/simple/manage.py test dummy_thumbnails --settings=settings.django_1_8 --traceback -v 3
python examples/simple/manage.py test dummy_thumbnails --settings=settings.testing --traceback -v 3
#./runtests.py
