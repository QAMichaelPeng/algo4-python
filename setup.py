from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='algos4-python',
    version='1.0',
    description='A python version of algo4',
    long_description=readme,
    author='QAMichaelPeng',
    author_email='pengfeng.git@gmail.com',
    packages=[],
    install_requires=[],  # external packages as dependencies
    scripts=[]
)
