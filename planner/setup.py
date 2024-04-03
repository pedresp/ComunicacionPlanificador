import os
from setuptools import find_packages, setup
from glob import glob

package_name = 'planificador'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.py'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gondolior',
    maintainer_email='pedro.espinosa@alumnos.upm.es',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'client = planificador.client:main',
            'server = planificador.service:main',
            'client2 = planificador.client2:main',
            'client3 = planificador.client3:main'
        ],
    },
)
