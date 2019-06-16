setup(
    name='fightml',
    version='0.0.1',
    description='html generator following directory structure you saved figures',
    long_description=readme,
    author='Kazeto Fukasawa',
    author_email='fukasawakaze@gmail.com',
    url='',
    license='MIT',
    install_requires=['numpy', 'pandas', 'jinja2', "matplotlib"]
    packages=find_packages(exclude=('tests', 'docs'))
)