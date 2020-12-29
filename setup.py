from setuptools import setup

setup(
    name='pomodoropy',
    version='v.0.0.2',
    packages=['pomodoropy'],
    url='',
    license='MIT',
    author='Josh Sarver',
    author_email='josh.sarver@gmail.com',
    description='Pomodoro timer for task',
    # data_files=["pomodoropy/images"],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pomodoro = pomodoropy.main:entry_point',
        ],
    }
)
# todo add dependencies
