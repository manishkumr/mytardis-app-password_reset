import os
from setuptools import setup, find_packages

version = '0.0.1'

setup(name='password_reset',
      version=version,
      description="MyTardis app to add password reset functionality",
      long_description="""\
Mytardis app to add password reset functionality for local account users\
""",
      classifiers=[],
      keywords='mytardis suthentication password reset',
      author='Manish Kumar',
      author_email='manish.kumar@monash.edu',
      url='',
      license='',
      packages=find_packages(),
      )