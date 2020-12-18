#!/usr/bin/env python

import os

from setuptools import setup

dir_path = os.path.dirname(os.path.realpath(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='demo_extension',
      version='1.0.0',
      author='Kodexa',
      description='An example of creating an extension pack to be deployed on the Kodexa platform.',
      author_email='lecia@kodexa.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/kodexa-ai/extension-pack-template',
      packages=['demo_extension'],
      include_package_data=True,
      install_requires=[
          'kodexa'
      ],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"])


# if you have requirements that need to be copied over for runtime use 
# (like the spaCy model in the runtime-requirements.txt example), place them in your runtime-requirements.txt file
# and uncomment the lines below
#import shutil    
#shutil.copy('runtime-requirements.txt','dist/runtime-requirements.txt') 
