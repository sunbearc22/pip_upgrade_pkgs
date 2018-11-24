#!/bin/python3

''' Upgrading only outdated "pip install --user" packages.'''

# Only python 3.5 and above may use this script because method subprocess.run()
# is used.

import subprocess
import sys


def get_outdated_pkgs():
    outdated_pkgs =[]
    try:
        cmd = [sys.executable, '-m', 'pip', 'list', '--user', '--outdated']
        completed = subprocess.run( cmd, check=True, stdout=subprocess.PIPE )
    except subprocess.CalledProcessError as err:
        print( 'ERROR:', err )
    else:
        outdated_pkgs=[ line for line in
                        completed.stdout.decode('utf-8').splitlines()[2:3] ]
        print('Outdated packages detected = {}.'.format(len(outdated_pkgs)) )
        print('Initiating upgrading...\n')
        return outdated_pkgs 
        

def upgrade_outdated_pkgs(outdated_pkgs):
    upgradelist = []
    errorlist = []
    count=0
    print('No. Package            Version           Latest           Type  Status  ') 
    print('--- ------------------ ----------------- ---------------- ----- --------')
    for i in outdated_pkgs:
        count += 1
        pkgname, ver, latest, setuptype = i.split()
        try:
            cmd = [sys.executable,'-m','pip','install','--upgrade','--user',
                   pkgname]
            completed = subprocess.run( cmd, check=True, stdout=subprocess.PIPE )
        except subprocess.CalledProcessError as err:
            errorlist.append(pkgname)
            print('{0:<4}{1:<19}{2:<18}{3:<17}{4:<6}{5:<8}'.format(
                count,pkgname,ver,latest,setuptype,'FAILED'))
            print( 'ERROR: {}'.format(err) )
        else:
            for line in completed.stdout.decode('utf-8').splitlines():
                if 'Successfully installed' in line:
                    upgradelist.append(pkgname)
                    print('{0:<4}{1:<19}{2:<18}{3:<17}{4:<6}{5:<8}'.format(
                        count,pkgname,ver,latest,setuptype,'UPGRADED'))
    return upgradelist, errorlist


def main():
    print('=====================================================')
    print('UPGRADING ALL OUTDATED "pip install --user" PACKAGES:')
    print('=====================================================')
    print()
    outdated_pkgs = get_outdated_pkgs() # created a list
    upgradelist, errorlist  = upgrade_outdated_pkgs(outdated_pkgs)
    total=len(outdated_pkgs)
    print('\nSUMMARY:')
    print('No. of packages upgraded = {}/{}'.format( len(upgradelist), total ))
    print('No. of upgrade errors    = {}/{}'.format( len(errorlist), total ))
    print()
    

if __name__ == '__main__':
    main()
