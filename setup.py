from setuptools import setup, find_packages
from os import path

project_root = path.abspath(path.dirname(__file__))
with open(path.join(project_root, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

print(readme)

setup(
    name='fightml',
    version='0.0.1',
    description='html generator following directory structure you saved figures',
    long_description=readme,
    author='Kazeto Fukasawa',
    author_email='fukasawakaze@gmail.com',
    url='https://github.com/kazetof/fightml',
    license='MIT',
    install_requires=['numpy', 'pandas', 'jinja2', "matplotlib"],
    packages=find_packages(exclude=('tests')),
    test_suite='tests'
)