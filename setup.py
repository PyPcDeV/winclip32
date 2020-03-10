import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="winclip32",
    version="0.6.0a",
    author="PyPcDeV",
    author_email="pypcdev@gmail.com",
    description="This is a small library for windows OS to work with clipboard data storage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PyPcDeV/winclip32",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'pywin32'
      ],
    python_requires='>=3.6',
)