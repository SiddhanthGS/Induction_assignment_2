import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'gazebo_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'models'), glob(os.path.join('models', 'new_world.sdf'))),
(os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'new.launch.py'))),
 (os.path.join('share', package_name, 'models'), glob(os.path.join('models', 'assn_2.sdf'))),
(os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'assn_2.launch.py'))),
(os.path.join('share', package_name, 'configs'), glob(os.path.join('configs', 'custom.rviz'))),
(os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'custom_rviz.launch.py'))),
#there might be extra comma required here

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='siddhanth',
    maintainer_email='siddhanth@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
