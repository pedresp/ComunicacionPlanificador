from setuptools import find_packages
from setuptools import setup

setup(
    name='syst_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('syst_msgs', 'syst_msgs.*')),
)
