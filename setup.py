from setuptools import find_packages, setup

setup(name='pyntc',
      version='0.0.1',
      packages=find_packages(),
      install_requires=['requests>=2.7.0',
                        'jsonschema',
                        'future',
                       ]
      )