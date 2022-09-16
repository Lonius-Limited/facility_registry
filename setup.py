from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in facility_registry/__init__.py
from facility_registry import __version__ as version

setup(
	name="facility_registry",
	version=version,
	description="Repository for all facility information and REST API resources",
	author="Lonis Limited",
	author_email="info@lonius.co.ke",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
