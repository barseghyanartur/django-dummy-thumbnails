import os

from setuptools import find_packages, setup

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
    readme = ''

version = '0.2.5'

install_requires = [
    'six>=1.4.1',
    'django-nine>=0.2.2',
]

extras_require = [
    'django-eximagination>=0.8',
    'feedparser'
]

tests_require = [
    'beautifulsoup4',
    'factory_boy',
    'fake-factory',
    'Pillow',
    'pytest',
    'pytest-django',
    'pytest-cov',
    'tox'
]

setup(
    name='django-dummy-thumbnails',
    version=version,
    description="Dummy thumbnails for most popular Django thumbnail "
                "generators.",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or "
        "later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords="django, django-dummy-thumbnails",
    author='Artur Barseghyan',
    author_email='artur.barseghyan@gmail.com',
    url='https://github.com/barseghyanartur/django-dummy-thumbnails/',
    package_dir={'': 'src'},
    packages=find_packages(where='./src'),
    license='GPL-2.0-only OR LGPL-2.1-or-later',
    install_requires=(install_requires + extras_require),
    tests_require=tests_require,
    include_package_data=True,
)
