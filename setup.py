from setuptools import setup
import os
from glob import glob

package_name = 'gazebo_tutorial'


def package_files(directory, patterns):
    files = []
    for pattern in patterns:
        files.extend(glob(os.path.join(directory, pattern)))
    return files


data_files = [
    ('share/ament_index/resource_index/packages',
     ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    (os.path.join('share', package_name, 'config'),
     package_files('config', ['*.yaml'])),
    (os.path.join('share', package_name, 'description'),
     package_files('description', ['*.xacro', '*.urdf'])),
    (os.path.join('share', package_name, 'launch'),
     package_files('launch', ['*.py'])),
    (os.path.join('share', package_name, 'worlds'),
     package_files('worlds', ['*.world'])),
]

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Josh Newans',
    maintainer_email='my_email@email.com',
    description='Virtual camera simulation package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)

