from pathlib import Path
from setuptools import find_packages, setup
README = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="whatthefunc",
    version='0.1.1',
    description="Python library to learn what a function/method/attribute does, explained by OpenAI's ChatGPT in layman's terms. Additional function to insert your own OpenAI API Key",
    long_description=README,
    long_description_content_type="text/markdown",
    author="ClavinK",
    author_email="ckama222@gmail.com",
    url="https://github.com/ClavinK/WhatTheFunc",
    license="MIT",
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    install_requires=["openai>=1.0.0"],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries",
        "Operating System :: OS Independent",
    ],
    keywords=["openai", "education", "explain", "python"],
)