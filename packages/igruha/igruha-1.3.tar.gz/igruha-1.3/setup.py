from setuptools import setup

long_description = open("README.md", "r", encoding='utf-8').read()

setup(
    name='igruha',
    version='1.3',
    packages=['igruha'],
    author='lordcodes',
    author_email='lordgrief176@gmail.com',
    description='Torrent-Igruha SDK Python',
    install_requires=['requests', 'lxml', 'beautifulsoup4'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
