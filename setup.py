import sys
import os
import yaml
import shutil
import subprocess
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

__package__ = "drones_cli"
__version__ = "0.0.0"

def fetch_repo(url: str, dest: Path) -> bool:
    """
    Wrapper function to fetch public github repo

    Args:
    - url: public url repo
    - dest: destination folder

    Return:
    - True: success
    - False: failure
    """

    if dest.exists():
        print(f"{dest.name} already there skipping clone.")
        return True

    try:
        print(f"Cloning into {dest}...")
        subprocess.run(["git", "clone", url, dest, "--recursive"], check=True, capture_output=False)
        print(f"Repository cloned successfully into {dest}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while cloning: {e}")
        return False

def pre_install_setup():
    """
    Setup before install package.

    The main idea of this pre-install setup is to fetch and prepare
    all the repositories and workspace for the package to operate.

    Setup:
    - Create working directory under /home/USER/.drones_cli
    - Clone PX4-Autopilot repo
    - Copy catalog.yml
    - Clone all the drone from the catalog
    - Auto-generate config.py module to populate package variables
    """
    if not sys.platform.startswith("linux"):
        sys.stderr.write("This package can only be installed on Linux.\n")
        sys.exit(1)

    WORK_DIR = Path().home() / f".{__package__}"
    WORK_DIR.mkdir(exist_ok=True)

    fetch_repo("https://github.com/PX4/PX4-Autopilot.git", WORK_DIR / "PX4-Autopilot")

    SOURCE_DIR = Path(__file__).parent.resolve()

    catalog_file = SOURCE_DIR / "catalog.yml"
    dest_catalog_file = WORK_DIR / "catalog.yml"

    # Always overwrite catalog in case is already present
    try:
        if dest_catalog_file.exists():
            os.remove(dest_catalog_file)
        shutil.copy(catalog_file, dest_catalog_file)
    except FileNotFoundError:
        raise Exception(f"Error: {catalog_file} not found!")
    except Exception as e:
        raise Exception(f"Error copying file: {e}")

    with dest_catalog_file.open('r') as file:
        config = yaml.safe_load(file)
        for drone, config in config["drones"].items():
            fetch_repo(config["url"], WORK_DIR / f"fw-{drone}")

    # Always overwrite `config.py` during auto-generation
    config_file = Path(__file__).parent.resolve() / __package__ / "config.py"
    with config_file.open("w") as f:
        f.write(f"## Auto-generated file. DO NOT EDIT !##\n")
        f.write(f"from pathlib import Path\n")
        f.write(f"from {__package__}.loader import Loader\n\n")
        f.write(f"WORK_DIR = Path(r'''{WORK_DIR}''')\n")
        f.write(f"CATALOG = Loader(WORK_DIR / 'catalog.yml').catalog\n")

class CustomInstallCommand(install):

    def run(self) -> None:
        pre_install_setup()
        super().run()


class CustomDevelopCommand(develop):

    def run(self) -> None:
        pre_install_setup()
        super().run()


setup(
    name=__package__,
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyyaml",
    ],
    cmdclass={
        "install": CustomInstallCommand,
        "develop": CustomDevelopCommand
    },
    package_data={
        f"{__package__}": ['catalog.yml']
    },
    entry_points={
        "console_scripts": [
            f"drones-cli = {__package__}.main:main",
        ],
    },
    python_requires=">=3.9",
)
