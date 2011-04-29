import os

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()
CHANGES = open(os.path.join(here, 'CHANGES')).read()

setup(name='kns',
      version='0.1',
      description='',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        ],
      author='Filia Tao',
      author_email='Filia.Tao@gmail.com',
      url='',
      keywords='knowledge,share',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'Django',
            'Django-Piston',
            ],
      tests_require=[
            #'BeautifulSoup',
            ],
      )

