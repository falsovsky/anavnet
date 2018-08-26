import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anavnet",
    version="0.0.1",
    author="Pedro de Oliveira",
    author_email="falsovsky@gmail.com",
    description="Client library to the AnavNet website, which provides messages about current portuguese ports warnings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='BSD-3-Clause',
    url="https://github.com/falsovsky/AnavNet",
    packages=setuptools.find_packages(exclude='tests'),
    install_requires=[
        'beautifulsoup4',
        'requests'
    ],
    scripts=[
        'bin/anavclient'
    ],
)
