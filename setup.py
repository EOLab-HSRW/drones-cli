import sys
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from eolab_px4 import __version__, __package__, CACHE_DIR

if not sys.platform.startswith("linux"):
    sys.stderr.write("This package can only be installed on Linux.\n")
    sys.exit(1)

setup(
    name=__package__,
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            f"{__package__} = eolab_px4.commands.eolab_px4:main",
        ],
    },
    python_requires=">=3.9",
)
