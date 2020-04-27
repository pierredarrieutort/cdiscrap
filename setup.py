from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cdiscrap",
    version="0.0.3",
    author="Mathieu Daix, Pierre Darrieutort",
    author_email="mathieudaixpro@gmail.com, p.darrieutort@outlook.com",
    description="Python package capable of raising the price of any product on the site www.cdiscount.com",
    url="https://github.com/pierredarrieutort/cdiscrap",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.2',
)
