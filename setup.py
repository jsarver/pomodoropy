from setuptools import setup, find_packages

setup(
    name='pomodoropy',
    version='0.0.4',
    packages=find_packages(),
    url='',
    license='MIT',
    author='Josh Sarver',
    author_email='josh.sarver@gmail.com',
    description='Pomodoro timer for task',
    include_package_data=True,
    install_requires=['pyside2', 'win10toast', 'pywin32==225'],
    entry_points={
        'gui_scripts': [
            'pomodoro = pomodoropy.main:entry_point',
        ],
    }
)
