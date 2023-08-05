from setuptools import find_packages, setup

setup(
    author="Mathias Schreiner",
    author_email="matschreiner@gmail.com",
    url="https://gitlab.com/matschreiner/pype",
    download_url="https://gitlab.com/matschreiner/pype/-/archive/v2.2.5/pype-v2.2.5.tar.gz",
    name="pype-ms",
    version="2.2.5",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
        "pytest",
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "pype = pype.cli:cli",
        ],
    },
)
