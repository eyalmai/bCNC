from setuptools import setup, find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name = "bCNC",
	version = "0.9.14.21",
	license="GPLv2",
	description='Swiss army knife for all your CNC/g-code needs',
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages = find_packages(),
	author = "Harvie",
	author_email='harvie@github.com',
	url="https://github.com/vlachoudis/bCNC",
	include_package_data=True,
	install_requires = [
		'pyserial>=3.4',
		'numpy>=1.15.4',
		'opencv-python>=3.4.2.17',
		'Pillow>=5.3.0',
	],

	entry_points = {
		'console_scripts': [
			#'bCNC = {package}.{module}:{main_function}',
			#'bCNC = bCNC.bCNC:main',
			'bCNC = bCNC.__main__:main',
		]
	},

	classifiers=[
		"Development Status :: 4 - Beta",
		"License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
		"Operating System :: OS Independent",
		"Topic :: Multimedia :: Graphics :: 3D Modeling",
		"Topic :: Multimedia :: Graphics :: Capture",
		"Topic :: Multimedia :: Graphics :: Editors :: Vector-Based",
		"Topic :: Multimedia :: Graphics :: Graphics Conversion",
		"Topic :: Multimedia :: Graphics :: Viewers",
		"Topic :: Scientific/Engineering",
		"Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
		"Topic :: Terminals :: Serial",
		"Natural Language :: Dutch",
		"Natural Language :: English",
		"Natural Language :: German",
		"Natural Language :: Spanish",
		"Natural Language :: Portuguese",
		"Natural Language :: Portuguese (Brazilian)",
		"Natural Language :: French",
		"Natural Language :: Italian",
		"Natural Language :: Japanese",
		"Natural Language :: Korean",
		"Natural Language :: Russian",
		"Natural Language :: Chinese (Simplified)",
		"Natural Language :: Chinese (Traditional)",
	]
)