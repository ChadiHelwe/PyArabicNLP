# from pip._internal.req import parse_requirements
# from pip._internal.download import PipSession
from distutils.extension import Extension
from setuptools import setup, find_packages, Extension
import os

from Cython.Distutils import build_ext
from Cython.Build import cythonize


def read_requirements():
    """parses requirements from requirements.txt"""
    install_reqs = parse_requirements("requirements.txt", session=PipSession())
    reqs = [str(ir.req) for ir in install_reqs]
    return reqs


with open("README.md", "r") as fh:
    long_description = fh.read()

ext_modules = [
    Extension("buckwalter", ["pyarabicnlp/transliteration/buckwalter.pyx"])
]

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
    python_requires=">=3.6",
    cmdclass={"build_ext": build_ext},
    ext_modules=cythonize(
        ext_modules, compiler_directives={"language_level": "3"}
    ),
)
