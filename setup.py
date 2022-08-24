# When we use setup.py we need -e . in requirements.txt file

from setuptools import setup, find_packages
from typing import List, Dict


def get_requirements_list()->List[str]:
    """
    This function is going to return a list of requirements from the requirements.txt file

    Returns: This function is hoing to return list which contains name of libraries 
    mentioned in requirement.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")

#Declaring variables for setup functions
# we can also declare variables initially and later assign them in setup function
NAME = 'housing_predictor'
REQUIREMENT_FILE_NAME = 'requirements.txt'

setup(
        name=NAME,
        version='0.0.3',
        author='Mohammed Ishtiaq',
        description='A housing price predictor',
        packages=find_packages(),
        install_requires=get_requirements_list()
)

# folder name is the name of the package and files are denoted as modules
# find_packages() is a function which is used to find all the packages in the folder
# and return a list of packages
# install_requires is a list of libraries that are required to run the package
