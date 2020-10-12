from setuptools import setup
import os

dir_setup = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_setup, 'cime', 'version.py')) as f:
    # Defines __version__
    exec(f.read())

with open("README.md", "r") as fh:
    long_description = fh.read()

# Current status: pre-alpha

setup(name='cime',
      version=__version__,
      description='A Python library for kinematic analysis of planar linkages (usable version is not available, this is completly experimental)',
      author='Pedro Jorge De Los Santos',
      author_email='delossantosmfq@gmail.com',
      license = "MIT",
      keywords=["Kinematics","Mechanism","Machinery","Linkages"],
      url='https://github.com/numython-rd/cime',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['cime'],
      classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Education",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: Implementation :: CPython",
      ]
      )
