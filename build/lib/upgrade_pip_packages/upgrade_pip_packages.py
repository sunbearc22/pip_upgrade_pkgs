#!/bin/python3

import subprocess
import sys
from pprint import pprint


def get_pkgs():
    try:
        cmd = [sys.executable, '-m', 'pip', 'list']
        completed = subprocess.run( cmd, check=True, stdout=subprocess.PIPE )
    except subprocess.CalledProcessError as err:
        print( 'ERROR:', err )
    else:
        for line in completed.stdout.decode('utf-8').splitlines()[2:5]:
            yield line


def upgrade_pkgs(piplist):
    packagelist = []
    upgradelist = []
    errorlist = []
    for i in piplist:
        pkgname, ver = i.split()
        packagelist.append(pkgname)
        print('\n',pkgname)
        try:
            cmd = [sys.executable, '-m', 'pip', 'install', '--upgrade',
                   '--user', pkgname]
            completed = subprocess.run( cmd, check=True, stdout=subprocess.PIPE )
        except subprocess.CalledProcessError as err:
            errorlist.append(pkgname)
            print( 'ERROR: {}'.format(err) )
        else:
            for line in completed.stdout.decode('utf-8').splitlines():
                print(line)
                if 'Successfully installed' in line:
                    upgradelist.append(pkgname)
    return packagelist, upgradelist, errorlist


def main():
    print('=============================================')
    print('UPGRADING ALL PIP PACKAGES TO LATEST VERSION:')
    print('=============================================')
    pip_pkgs = get_pkgs() # created a generator
    packagelist, upgradelist, errorlist  = upgrade_pkgs(pip_pkgs)
    print('\nSummary:')
    print('No. of pip  packages  = {}'.format( len(packagelist) ))
    print('No. of upgrades       = {}'.format( len(upgradelist) ))
    print('No. of upgrade errors = {}'.format( len(errorlist) ))
    if upgradelist:
        print('Package(s) upgraded:')
        pprint(upgradelist)
    if errorlist:
        print('Package(s) with upgrade error:')
        pprint(errorlist)
    print()
    

if __name__ == '__main__':
    sys.exit( main() )
