from setuptools import setup, find_packages
from typing import List

#Declaring variable
REQUIREMENT_FILE_NAME = 'requirements.txt'

HYPEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirements mentioned in
    requirements.txt file

    return: This function is going to return a list containing  names of libraries
    required for the project
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace('\n',"") for requirement_name in requirement_list]
        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)
        return requirement_list

setup(
    name = 'housing-predictor',
    version = '0.0.1',
    author = 'Shashvath N',
    description='Housing price prediction - Regression Task',
    packages = find_packages(),
    install_requires = get_requirements_list()
)
