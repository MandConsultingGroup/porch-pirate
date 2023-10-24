#!/usr/bin/python3
import setuptools
from distutils.core import setup
from os import path
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='porch-pirate',
      version='0.0.1',
      description='Porch Pirate is a recon client and framework that facilitates the discovery and exploitation of API endpoints and secrets committed to public Postman workspaces, collections, requests, users and teams. Porch Pirate can be used as a client or be incorporated into your own applications."',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Mand Consulting Group / zer0pwn',
      author_email='zer0pwn@riseup.net',
      keywords='porchpirate porch pirate porch-pirate postman postmaniac osint recon enumeration secrets loot treasure',
      url='https://github.com/mandconsultinggroup/porch-pirate',
      packages=['porchpirate'],
      scripts=['bin/porch-pirate'],
      install_requires=['requests']
     )