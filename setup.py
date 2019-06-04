import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvector-pkg-jonathasg",
    version="0.0.1",
    author="Jônathas Gouveia",
    author_email="jonathas_gouv@hotmail.com",
    description="A vector module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonathasgouv/pyvector",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
)