# -*- coding: utf-8 -*-

#  Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
#  License: BSD 3-Clause License

import setuptools

import Linked_List_lib

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    required = fh.read().splitlines()

setuptools.setup(
    name="Linked_List_lib",
    version=Linked_List_lib.__version__,
    author="Daniel Yang",
    author_email="daniel.yj.yang@gmail.com",
    description="Library for Studying and Applying Linked List Data Structure",
    license=Linked_List_lib.__license__,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/daniel-yj-yang/Linked_List_lib",
    packages=setuptools.find_packages(),
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    python_requires='>=3.8',
    include_package_data=True,
)
