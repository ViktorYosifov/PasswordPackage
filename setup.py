from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "PasswordPackage"
LONG_DESCRIPTION = "Password Manager package generating a secure password and encrypting it"

setup(
    name="passman",
    version=VERSION,
    author="Viktor Yosifov",
    author_email="<viktoryosifov@email.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],

    keywords=['python', 'passman'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)