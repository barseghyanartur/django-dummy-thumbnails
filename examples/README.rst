=============================================
Example project for `django-dummy-thumbnails`
=============================================
Follow instructions below to install the example project. Commands below are
written for Ubuntu/Debian, but may work on other Linux distributions as well.

(1) Create a new- or switch to existing- virtual environment.

    .. code-block:: sh

        virtualenv django-dummy-thumbnails

        source django-dummy-thumbnails/bin/activate

(2) Download the latest stable version of django-dummy-thumbnails:

    .. code-block:: sh

        wget https://github.com/barseghyanartur/django-dummy-thumbnails/archive/stable.tar.gz

(3) Unpack it somewhere.

    .. code-block:: sh

        tar -xvf stable.tar.gz

(4) Go to the unpacked directory.

    .. code-block:: sh

        cd django-dummy-thumbnails-stable

(5) Install Django, requirements and django-dummy-thumbnails.

    .. code-block:: sh

        pip install -r requirements.txt

        pip install https://github.com/barseghyanartur/django-dummy-thumbnails/archive/stable.tar.gz

(6) Create some directories.

    .. code-block:: sh

            mkdir -p examples/media/static/ examples/static/ examples/db/ examples/logs

(7) Copy local_settings.example

    .. code-block:: sh

    cp examples/simple/settings/local_settings.example examples/simple/settings/local_settings.py

(8) Run the commands to sync database, collect static files, make necessary
    symlinks.

    .. code-block:: sh

        ./manage.py migrate --noinput --traceback -v 3

        ./manage.py collectstatic --noinput --traceback -v 3

        ./manage.py dummy_thumbnails_symlink_dummy_images

        python examples/simple/manage.py runserver 0.0.0.0:8000 --traceback -v 3

(9) Run the server.

    Using Django's own runner.

    .. code-block:: sh

        python examples/simple/manage.py runserver 0.0.0.0:8000 --traceback -v 3

    Or using gunicorn:

    .. code-block:: sh

        gunicorn examples.simple.wsgi

(10) Open your browser and test the app.

    .. code-block:: text

            - URL: http://127.0.0.1:8000/
