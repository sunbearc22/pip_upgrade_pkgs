from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    #Primary info
    name="upgrade_pip_packages",
    version="0.0.1rc3", #PEP440
    packages=find_packages(),

    #Project description
    long_description=long_description,
    long_description_content_type="text/markdown",

    #Project links
    url="https://github.com/sunbearc22/upgrade_pip_packages", # project home page, if any

    #Meta
    description="Upgrade all installed pip packages to latest version.",
    license="MIT",
    keywords="pip pip3 upgrade packages",
    python_requires='~=3.5',
    install_requires=['pip~=18.0'],

    #Maintainers
    author="sunbearc22",
    author_email="sunbear.c22@gmail.com",

    # Classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
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
            'upgrade_pip_packages=upgrade_pip_packages.upgrade_pip_packages:main',
            ],
        },

)
