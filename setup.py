""" pylavi package info
    See: https://setuptools.pypa.io/en/latest/setuptools.html#command-reference
    See: https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/
"""


import os
import re
from setuptools import setup, find_packages


VERSION_PATTERN = re.compile(
    r"^\s*__version__\s*=\s*['\"](\d+\.\d+\.\d+)['\"]", re.MULTILINE
)


def get_file_contents(*filename):
    """Get the contents of a file relative to the directory setup.py is in"""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(this_dir, *filename)

    if os.path.isfile(readme_path):
        with open(readme_path, "r", encoding="utf-8") as readme:
            return readme.read().strip()

    return ""


def get_version():
    """single-source the version by reading the __init__.py file"""
    metadata = get_file_contents("pylavi", "__init__.py")
    has_version = VERSION_PATTERN.search(metadata)

    if not has_version:
        raise RuntimeError("Unable to find version string.")

    return has_version.group(1)


setup(
    name="pylavi",
    version=get_version(),
    description="Python LabVIEW File Parser",
    long_description=get_file_contents("README.md"),
    long_description_content_type="text/markdown",
    author="marcpage",
    author_email="MarcAllenPage@gmail.com",
    install_requires=[],
    python_requires="",
    url="https://github.com/marcpage/pylavi",
    license="Unlicense",
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
        "Topic :: Software Development",
    ],
    keywords=(
        "labview vi mnu ctl instruments parser extractor "
        + "reverse-engineering development"
    ),
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "lv_assembler = pylavi.assembler:main",
            "vi_validate = pylavi.validate:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/marcpage/pylavi/issues",
        "Source": "https://github.com/marcpage/pylavi/",
    },
)
