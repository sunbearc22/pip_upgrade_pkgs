from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    #Require fields
    name="pip_upgrade_pkgs",
    version="0.0.1", #PEP440
    packages=find_packages(),

    #Project description
    long_description=long_description,
    long_description_content_type="text/markdown",

    #Project links
    url="https://github.com/sunbearc22/pip_upgrade_pkgs", # project home page, if any

    #Meta
    description='A single command to upgrade outdated "pip install --user" packages.',
    license="MIT",
    keywords="pip upgrade packaging",
    python_requires='~=3.5',
    install_requires=['pip~=18.0'],
    setup_requires=['pip~=18.0'],

    #Maintainers
    author="sunbearc22",
    author_email="sunbear.c22@gmail.com",

    # Classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Archiving :: Packaging",
        "Environment :: Console ",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        ],

    #Automatic script creation
    #console_script syntax is [command=package_name.module_name:function]
    entry_points={
        'console_scripts': [
            'pip_upgrade_pkgs=pip_upgrade_pkgs.pip_upgrade_pkgs:main',
            ],
        },

)
