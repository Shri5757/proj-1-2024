from setuptools import setup, find_packages


def get_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
        return requirements


setup(
    name='ml-project',
    version='0.0.1',
    author='shrikant',
    author_email='shrikantdhumal1996@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)