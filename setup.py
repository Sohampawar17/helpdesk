from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in helpdesk/__init__.py
from helpdesk import __version__ as version

setup(
	name="helpdesk",
	version=version,
	description="Helpdesk for mobile applicaion",
	author="Quantbit Technologies",
	author_email="contact@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
