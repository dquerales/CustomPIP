from setuptools import setup

setup(
    name="pyexample",
    version="0.1.0",
    description="A example Python package",
    url="https://github.com/dquerales/CustomPIP",
    author="Daniel Querales",
    author_email="dquerales@gmail.com",
    packages=["pyexample"],
    install_requires=[
        "pandas>=1.5.3",
    ],
)
