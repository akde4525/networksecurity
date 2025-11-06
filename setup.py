from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """Reads the requirements from a file and returns them as a list."""
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines=file.readlines()
            # Process each line to remove whitespace
            for line in lines:
                requirement=line.strip()
                # Ignore empty lines and -e . entries
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst 

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Akash Dey",
    author_email="akde4525@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)                 