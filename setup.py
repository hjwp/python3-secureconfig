from setuptools import setup, find_packages
#from distutils.extension import Extension

import os
os.environ['ARCHFLAGS'] = '-Wno-error=unused-command-line-argument-hard-error-in-future'


setup(
    name="secureconfig",
    version="0.1.4c",
    description="Configuration-oriented encryption toolkit to make secure config files simple",
    url="https://bitbucket.org/nthmost/python-secureconfig",
    author="Naomi Most",
    author_email="naomi@nthmost.net",
    maintainer="Naomi Most",
    maintainer_email="naomi@nthmost.net",
    license="MIT",
    zip_safe=True,
    packages=find_packages(),
    install_requires=['cryptography'],
)

