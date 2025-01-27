#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "pydantic>=1.5.1",
    "aiosmtplib>=1.1.3"
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Lars Claussen",
    author_email='claussen.lars@nelen-schuurmans.nl',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='async_mail',
    name='async_mail',
    packages=find_packages(include=['async_mail', 'async_mail.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/larsclaussen/async_mail',
    version='0.1.1',
    zip_safe=False,
)
