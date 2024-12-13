from setuptools import setup, find_packages
from SPyderSQL import __meta__


setup(
    name="SPyderSQL",
    version=__meta__.__version__,
    author=__meta__.__author__,
    author_email=__meta__.__email__,
    description=__meta__.__description__,
    long_description=open("README.rst", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url=__meta__.__url__,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests>=2.25.1",
        "numpy>=1.19.0",
        "pytest>=6.2.5",
        "flake8>=3.9.2"
    ],
    python_requires=">=3.6",
)
