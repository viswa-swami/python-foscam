#!/usr/bin/python

from setuptools import setup, find_packages
import os


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Customer Service',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Telecommunications Industry',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Multimedia :: Sound/Audio',
    'Topic :: Utilities',
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
]

setup(
    name='pyfoscam',
    version='1.0',
    description='Python Library for Foscam IP Cameras',
    long_description=open('README.rst', 'r').read(),
    author='Viswanathan S',
    author_email='viswa.swami@gmail.com',
    url='https://github.com/viswa-swami/python-foscam',
    include_package_data=True,
    license='LGPLv3+',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    keywords=['foscam', 'Camera', 'IPC'],
)
