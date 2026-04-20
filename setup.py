"""
The setup.py file is an essential part of packaging and distributing
Python projects. It is used by setuptools to define the configuration
of your project such as metadata, dependencies, and more.
"""

from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function reads requirements.txt and returns a clean list
    of dependencies.
    """
    requirements: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                # Ignore empty lines and editable installs like '-e .'
                if requirement and not requirement.startswith("-e"):
                    requirements.append(requirement)

    except FileNotFoundError:
        raise FileNotFoundError("requirements.txt file not found")

    return requirements


setup(
    name="Creditworthiness",
    version="0.0.1",
    author="Irfan",
    author_email="if476771@gmail.com",   # FIXED
    description="Credit risk prediction ML pipeline",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.8"
)