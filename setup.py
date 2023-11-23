from setuptools import setup, find_packages

setup(
    name='winged-python',
    version='0.1.0',
    description='Winged-Python is an innovative Domain-Specific Language (DSL) library for efficient HTML writing in Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Michel Anderson Lutz Teixeira',
    author_email='michel_lutz@icloud.com',
    url='https://github.com/micheltlutz/winged-python',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
)
