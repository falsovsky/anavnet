import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anavnet",
    version="0.0.2",
    author="Pedro de Oliveira",
    author_email="falsovsky@gmail.com",
    description="Client library to the AnavNet website, which provides the current warnings from the Portuguese maritime ports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='BSD-3-Clause',
    url="https://github.com/falsovsky/anavnet",
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=setuptools.find_packages(exclude='tests'),
    install_requires=[
        'beautifulsoup4',
        'requests'
    ],
    scripts=[
        'bin/anavclient'
    ],
)
