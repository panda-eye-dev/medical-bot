#So, this prject becomes a package
from setuptools import find_packages, setup

setup(
    name="medical_chatbot",
    version='0.1.0',
    author='Payal K',
    author_email='pk@gmail.com',
    packages=find_packages(),
    install_requires=[]
)