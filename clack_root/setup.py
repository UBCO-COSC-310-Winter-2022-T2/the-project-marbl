from setuptools import setup, find_packages

setup(
    name='CLACK',
    version='0.1.0',
    packages=find_packages(),
    # install_requires=[
    #     'numpy',
    #     'matplotlib'
    # ],
    entry_points={
        'console_scripts': [
            'start=clack_root.back_end:main'
        ]
    }
)
