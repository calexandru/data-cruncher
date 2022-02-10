from setuptools import setup

setup(
    name="wfcli",
    version="0.1.0",
    packages=["wayf"],
    author="Cristi P",
    author_email="cristian.alexandru86@gmail.com",
    package_data={"": ["input/default.txt"]},
    include_package_data=True,
    entry_points={"console_scripts": ["wfcli = wayf.cli:main"]},
)
