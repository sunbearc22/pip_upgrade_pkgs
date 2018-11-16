# upgrade_pip_packages

A `python 3.5+` package to upgrade all installed `pip` packages to the latest version.<br/>

```
=============================================
UPGRADING ALL PIP PACKAGES TO LATEST VERSION:
=============================================
.
.
.

SUMMARY:
Pre-installed pip packages = 145
No. of upgrades            = 5
No. of upgrade errors      = 2
Package(s) upgraded:
['beautifulsoup4', 'bleach', 'blinker', `chardet`, 'checkbox-support']
Package(s) with upgrade error:
['pycups', 'pycurl']
```

## Install Requirements
`python 3.5, 3.6, 3.7`<br/>
`pip` <br/>

## OS
`Ubuntu 16.04 (Xenial)` - Tested <br/>

## Installation
Call up a terminal, i.e. a command-line interface (cli) by press Ctrl+Alt+T, and submit this command:
`$ pip install --user upgrade_pip_packages`

- For `python3.5`, the modules of this package are installed in your directory `~/.local/lib/python3.5/site-packages/upgrade_pip_packages`
- The execution script of this package is installed in your directory `~/.local/bin/upgrade_pip_packages` .

## Execution:
Submit this terminal command:
```
$ upgrade_pip_packages
```

## Tests
Tested with `python 3.5` and `pip 18.1` in OS `Ubuntu 16.04`. <br/>

