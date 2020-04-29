from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cdiscountpriceparser',
    version='0.0.1',
    description='price parser of cdiscount product.',
    py_modules=["price_parser"],
    package_dir={'': 'cdiscount'},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "beautifulsoup4 ~= 4.9.0",
        "urllib3 ~= 1.25.9",
        "regex ~= 2020.4.4"
    ],
    extras_require={
        "dev": [
            "pytest>=5.4.1"
        ]
    },
    url="https://github.com/pierredarrieutort/cdiscrap",
    author="mathieudaix, pierredarrieutort",
    author_email="mathieudaixpro@gmail.com, p.darrieutort@outlook.fr"
)
