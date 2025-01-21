from setuptools import setup, find_packages

setup(
    name="eolab_px4",
    version="0.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "eolab_px4=eolab_px4:main",
        ],
    },
)
