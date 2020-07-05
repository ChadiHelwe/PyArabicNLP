from distutils.extension import Extension
from setuptools import setup, find_packages, Extension
import os

def read_requirements():
    """parses requirements from requirements.txt"""
    install_reqs = open("requirements.txt", "r").readlines()
    reqs = [str(ir).strip() for ir in install_reqs]
    print(reqs)
    return reqs


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyarabicnlp",  # Replace with your own username
    version="0.0.2",
    author="Chadi Helwe",
    author_email="chadi.helwe@gmail.com",
    description="PyArabicNLP: A Python library for Arabic NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChadiHelwe/PyArabicNLP/",
    install_requires=read_requirements(),
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="==3.7",
)
