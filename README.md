# upgrade_pip_packages

A python 3 script to upgrade all pip --user packages to the latest version.<br/>
Tested with python 3.5 and pip 18.1 via idle-python3.5 and terminal. <br/>

## Execution:
1. Download script.<br/>
2. Run script:<br/>
    2.1. via _idle-python3.5_:  Open script and press F5, or <br/>
    2.2. via _terminal_: Issue command `python3 -m upgrade_pip_packages`<br/>

## Example of Final Output:
```
No. of pip --user packages = 145
No. of upgrades            = 5
No. of upgrade errors      = 2
Package(s) upgraded:
['beautifulsoup4', 'bleach', 'blinker', `chardet`, 'checkbox-support']
Package(s) with upgrade error:
['pycups', 'pycurl']
```
