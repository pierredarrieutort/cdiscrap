import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cdiscrap",
    version="0.0.1",
    author="Pierre Darrieutort, Mathieu Daix",
    author_email="p.darrieutort@outlook.fr, mathieudaixpro@gmail.com",
    description="A pretty package for cdiscount price parser",
    url="https://github.com/pierredarrieutort/cdiscrap",
    packages=setuptools.find_packages(include=['scrap.py']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.2',
    scripts=['cdiscount.price_parser/scrap.py']
)
