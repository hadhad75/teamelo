# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.mkd') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='simpleapi',
    version='0.1.0',
    description='Exemple d\'API en Python',
    long_description=readme,
    author='Adrien Vossough',
    author_email='adrien@semifir.com',
    url='https://www.semifir.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements,
#    packages=['src']
)