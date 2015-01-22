#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='docker_builder',
    version='0.1',
    description='Builder for docker containers',
    url = '',
    author='zbal',
    author_email='vincent@wiredcraft.com',
    license='MIT',
    package_dir={
        'docker_builder': '.'
    },
    packages=[
       'docker_builder'
    ],
    scripts=[
        'bin/docker-builder'
    ]
)
