"""Python setup.py for dlg_nifty_components package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("dlg_nifty_components", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="dlg_nifty_components",
    version=read("dlg_nifty_components", "VERSION"),
    description="Awesome dlg_nifty_components created by ICRAR",
    url="https://github.com/ICRAR/dlg-nifty-components/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="ICRAR",
    license="BSD License",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["dlg_nifty_components = dlg_nifty_components.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
