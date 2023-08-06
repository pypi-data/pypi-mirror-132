from setuptools import setup, find_packages

from pyhhmm import __version__

extra_test = [
    'pytest>=6',
]

extra_dev = [
    *extra_test,
]

setup(
    name='pyhhmm',
    version=__version__,
    description='PyHHMM - Python implementation of HMM with labels',

    url='https://github.com/fmorenopino/HeterogeneousHMM',
    author='Emese Sukei, Fernando Moreno-Pino',
    author_email='esukei@tsc.uc3m.es, fmoreno@tsc.uc3m.es',

    packages=find_packages(),

    extras_require={
        'test': extra_test,
        'dev': extra_dev,
    },

    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
)
