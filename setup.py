from setuptools import setup, find_packages

setup(
    name='pomodoropy',
    version='v.0.0.3',
    packages=find_packages(),
    url='',
    license='MIT',
    author='Josh Sarver',
    author_email='josh.sarver@gmail.com',
    description='Pomodoro timer for task',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pomodoro = pomodoropy.main:entry_point',
        ],
    }
)
# todo add dependencies
