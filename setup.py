from setuptools import setup, find_packages

setup(
    name="scheduler_redis",
    version="0.1",
    description="proyecto de prueba",
    author="Luis Alonso Ballena Garcia",
    author_email='alonsoballena@gmail.com',
    license="GPL",
    packages=find_packages(),
    install_requires=[i.strip() for i in open("requirements.txt").readlines()]
)
