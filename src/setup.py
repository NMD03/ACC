from setuptools import setup, find_packages

setup(
    name="acc",
    version=0.1,
    packages=find_packages(),
    install_requires=[

    ],
    entry_points={
        "console_scripts": [
            "acc = acc.main:main",
        ],
    },
    author="Niclas Dauster",
    description="An advanced command line calculator"
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NMD03/acc",
)
