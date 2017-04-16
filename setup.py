from setuptools import setup

setup(
    name =         'draftlog',
    version =      '2.0.9',
    description =  'Create updatable log lines into the terminal.',
    url =          'https://github.com/kepoorhampond/python-draftlog',
    author =       'Kepoor Hampond',
    author_email = 'kepoorh@gmail.com',
    license =      'MIT',
    packages =     ['draftlog'],
    install_requires= [
        'colorama'  # This package will ensure ANSI support for windows cmd
    ],
)
