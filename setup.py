from setuptools import setup

setup(
    name='passwords',
    version='1.0',
    license='MIT',
    description='generate rememberable passwords from cli',
    author='Lars Mueller',
    author_email='me@larsmuellerme',
    url='larsmueller.me/passwords',
    py_modules=['passwords'],
    entry_points={
        'console_scripts': ['passwords = passwords:__init__', ],
    },
    long_description=open('README.md').read(),


)