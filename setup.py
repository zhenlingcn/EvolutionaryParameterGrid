# !/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='EvolutionaryParameterGrid',
    version='0.0.4',
    author='ZhangHengzhe',
    author_email='',
    description='Use evolutionary algorithms instead of GridParameter in scikit-learn.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
    ],
    package_dir={'': '.'},
    packages=find_packages('.'),
    install_requires=[
        'numpy>=1.9.3',
        'scipy>=0.16.0',
        'deap>=1.0.2',
        'scikit-learn>=0.18.0',
    ],
)
