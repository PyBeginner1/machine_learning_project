from setuptools import setup
from typing import List

#Declaring variable
REQUIREMENT_FILE_NAME = 'requirements.txt'

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirements mentioned in
    requirements.txt file

    return: This function is going to return a list containing  names of libraries
    required for the project
    """
    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
    name = 'housing-predictor',
    version = '0.0.1',
    author = 'Shashvath N',
    description='Housing price prediction - Regression Task',
    packages = ['housing'],
    install_requires = get_requirements_list()
)
