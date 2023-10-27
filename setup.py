from setuptools import find_packages, setup

setup(
    name='dsvalloureclib',
    packages=find_packages(include=['dsvalloureclib']),
    version='0.1.0',
    install_requires=['scikit-learn'],
    description='My first Python library',
    author='Me',
)