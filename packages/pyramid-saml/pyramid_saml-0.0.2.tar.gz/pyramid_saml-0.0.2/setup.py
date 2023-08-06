# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

requires = [
    'pyramid',
    'python3-saml'
]

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

with open(os.path.join(here, 'CHANGELOG.md')) as f:
    long_description += '\n\n'
    long_description += f.read()

setup(
    name='pyramid_saml',
    version='0.0.2',
    description='Pyramid SAML',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Karsten Deininger',
    author_email='karsten.deininger@bl.ch',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP'
    ],
    url='https://gitlab.com/geo-bl-ch/pyramid_saml',
    keywords='web pyramid saml',
    install_requires=requires,
    packages=find_packages(exclude=['demo', 'test*']),
    include_package_data=True
)
