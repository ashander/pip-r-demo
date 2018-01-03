from setuptools import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='make-rstudio-project',
    version='0.0.1',
    author='jaime ashander',
    author_email='at ucla dot edu',
    packages=['make_rstudio_project'],
    url='https://github.com/ashander/pip-r-demo',
    license='GPLv3',
    description='Make an Rstudio project with R',
    long_description=long_description,
    scripts=['bin/mkrproj'],
)
