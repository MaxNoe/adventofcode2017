from setuptools import setup, find_packages
from Cython.Build import cythonize


setup(
    name='adventofcode2017',
    author='Maximilian Noethe',
    author_email='maximilian.noethe@tu-dortmund.de',
    packages=find_packages(),
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    install_requires=['requests'],
    ext_modules=cythonize('adventofcode2017/*.pyx'),
)
