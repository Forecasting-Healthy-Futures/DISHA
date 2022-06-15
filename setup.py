import pathlib
import pkg_resources
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

with pathlib.Path("requirements.txt").open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]

VERSION = '1.1'
PACKAGE_NAME = 'DISHA'
AUTHOR = 'rishabhdev070'
AUTHOR_EMAIL = 'rishabhdev070@gmail.com'
URL = 'https://github.com/Forecasting-Healthy-Futures/DISHA'

LICENSE = "Apache License 2.0"
DESCRIPTION = 'Data Integrated solutions for healthy futures with AI'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
# LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numpy',
      'requests',
      'geopy',
      'tensorflow',
      'sklearn',
      'pandas',
      'matplotlib',
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      classifiers=[
            "Programming Language :: Python :: 3.8",
            "Operating System :: OS Independent"
      ],

      install_requires=INSTALL_REQUIRES,
      include_package_data=True,
      package_dir={"": "DISHA"},
      packages=find_packages(where="src"),
      python_requires=">=3.6"
      )