from setuptools import setup, find_packages

setup(
    name='CLACK',
    version='0.2.7',
    packages=find_packages(),
    # install_requires=[
    #     'numpy',
    #     'matplotlib'
    # ],
    entry_points={
        'console_scripts': [
            'start=UI.main:main',
        ]
    }
)