from setuptools import setup, find_packages

setup(
    name = 'slf-project-one',
    version = '0.1dev',
    packages = find_packages(),
    license = 'BSD',
    long_description = open('README.rst').read(),

    # This causes the main function in project_one to be run when the
    # project_one command is executed.
    # Use this when setup.py should install an executable command.
    entry_points={
        'console_scripts': [
            'project_one = project_one.project_one:main',
        ],
    },
)
