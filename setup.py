import os, distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup, find_packages

readme = os.path.join(os.path.dirname(__file__), 'README')
long_description = open(readme).read()

setup(
    name = "python-postmark",
    version = "0.2.0",
    packages = find_packages(),
    
    author = "Dave Martorana & Richard Cooper",
    # license = 'BSD',
    description = "Postmark library for Python 2.4 and greater.",
    long_description = long_description,
    url = "http://github.com/themartorana/python-postmark",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)