echo 'Making messages for django-dummy-thumbnails...'
cd src/dummy_thumbnails/
django-admin.py makemessages -l de
django-admin.py makemessages -l nl
django-admin.py makemessages -l ru

echo 'Making messages for example projects...'
cd ../../examples/simple/
django-admin.py makemessages -l de
django-admin.py makemessages -l nl
django-admin.py makemessages -l ru
