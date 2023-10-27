from setuptools import find_packages, setup

setup(
    name='dsvallourec-lib',
    packages=find_packages(include=['dsvallourec-lib']),
    version='0.1.0',
    install_requires=['scikit-learn'],
    description='My first Python library',
    author='Me',
)