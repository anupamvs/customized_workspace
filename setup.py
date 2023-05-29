from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customized_workspace/__init__.py
from customized_workspace import __version__ as version

setup(
	name="customized_workspace",
	version=version,
	description="Customized Workspace for Frappe",
	author="Anupam",
	author_email="hello@anupamvs.dev",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
