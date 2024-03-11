from setuptools import find_packages, setup

package_name = 'establish_middle'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'joselin = establish_middle.simple_sim_comm:main',
            'juanin = establish_middle.simple_sim_receiv:main'
        ],
    },
)
