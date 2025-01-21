from setuptools import setup, find_packages

setup(
    name='no40',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'azure-identity',
        'azure-mgmt-resource',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'no40=no40.cli:cli'
        ]
    },
)

