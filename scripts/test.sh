reset
#./scripts/uninstall.sh
#./scripts/install.sh
python examples/simple/manage.py test dummy_thumbnails --traceback -v 3 --settings=settings.testing
