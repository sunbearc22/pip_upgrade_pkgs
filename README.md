# pip_upgrade_pkgs

A single command to upgrade outdated `pip install --user` packages.

```
$ pip_upgrade_pkgs
=====================================================
UPGRADING ALL OUTDATED "pip install --user" PACKAGES:
=====================================================

Outdated packages detected = 16.
Initiating upgrading...

No. Package            Version         Latest          Type  Status
--- ------------------ --------------- --------------- ----- --------
1   Cython             0.29             0.29.1         wheel UPGRADED
2   ipython            6.2.1            7.1.1          wheel UPGRADED
3   ipywidgets         7.0.5            7.4.2          wheel UPGRADED
4   jupyter-client     5.1.0            5.2.3          wheel UPGRADED
5   jupyter-console    5.2.0            6.0.0          wheel UPGRADED
6   matplotlib         2.1.0            3.0.2          wheel UPGRADED
7   numpy              1.15.1           1.15.4         wheel UPGRADED
8   pandas             0.21.0           0.23.4         wheel UPGRADED
9   Pillow             5.2.0            5.3.0          wheel UPGRADED
10  qtconsole          4.3.1            4.4.3          wheel UPGRADED
11  setuptools         40.0.0           40.6.2         wheel UPGRADED
12  sympy              1.1.1            1.3            sdist UPGRADED
13  virtualenv         16.0.0           16.1.0         wheel UPGRADED
14  virtualenv-clone   0.3.0            0.4.0          wheel UPGRADED
15  wheel              0.31.1           0.32.3         wheel UPGRADED
16  youtube-dl         2018.9.26        2018.11.23     wheel UPGRADED

SUMMARY:
No. of packages upgraded = 16/16
No. of upgrade errors    = 0/16
```

## Install Requirements

python 3.5, 3.6, 3.7
pip~=18.0

## OS

Ubuntu 16.04 (Xenial) and above

## Installation
Submit this terminal command:

    $ pip install --user pip_upgrade_pkgs

For python3.5: 

- this package will be installed in ~/.local/lib/python3.5/site-packages/pip_upgrade_pkgs

- this package execution script will be installed in ~/.local/bin/pip_upgrade_pkgs.

## Execution:
Submit this terminal command:

    $ pip_upgrade_pkgs

or, access its module and execute its main() function:

    $ python3
    Python         3.5.2 (default, Nov 12 2018, 13:43:14)
    [GCC 5.4.0 20160609] on linux
    Type     "help", "copyright", "credits" or "license" for more information.
    >>> import pip_upgrade_pkgs
    >>> pip_upgrade_pkgs.main()



