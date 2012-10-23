#!/usr/bin/env python

import os
import re
import subprocess
import sys

modified = re.compile('^(?:M|A)(\s+)(?P<name>.*)')

CHECKS = [
    {
        'output': 'Checking for pdbs...',
        'command': 'grep -n "import pdb" %s',
        'ignore_files': ['.*pre-commit'],
        'print_filename': True,
    },
    {
        'output': 'Checking for ipdbs...',
        'command': 'grep -n "import ipdb" %s',
        'ignore_files': ['.*pre-commit'],
        'print_filename': True,
    },
    {
        'output': 'Checking for print statements...',
        'command': 'grep -n print %s',
        'match_files': ['.*\.py$'],
        'ignore_files': ['.*migrations.*', '.*management/commands.*', '.*manage.py', '.*/scripts/.*'],
        'print_filename': True,
    },
    {
        'output': 'Checking for console.log()...',
        'command': 'grep -n console.log %s',
        'match_files': ['.*yipit/.*\.js$'],
        'print_filename': True,
    },
    {
        'output': 'Checking for debugger...',
        'command': 'grep -n debugger %s',
        'match_files': ['.*\.js$'],
        'print_filename': True,
    },
    {
       'output': 'Running Jshint...',
       # By default, jshint prints 'Lint Free!' upon success. We want to filter this out.
       'command': 'jshint %s | grep -v "Lint Free!"',
       'match_files': ['.*yipit/.*\.js$'],
       'print_filename': False,
    },
    {
        'output': 'Running Pyflakes...',
        'command': 'pyflakes %s',
        'match_files': ['.*\.py$'],
        'ignore_files': ['.*settings/.*', '.*manage.py', '.*migrations.*', '.*/terrain/.*'],
        'print_filename': False,
    },
    {
        'output': 'Running pep8...',
        'command': 'pep8 -r --ignore=E501,W293 %s',
        'match_files': ['.*\.py$'],
        'ignore_files': ['.*migrations.*'],
        'print_filename': False,
    },
    {
        'output': 'Checking for Sass changes...',
        'command': 'sass --quiet --update %s',
        'match_files': ['.*\.scss$'],
        'print_filename': True,
    },
]


def matches_file(file_name, match_files):
    return any(re.compile(match_file).match(file_name) for match_file in match_files)


def check_files(files, check):
    result = 0
    print check['output']
    for file_name in files:
        if not 'match_files' in check or matches_file(file_name, check['match_files']):
            if not 'ignore_files' in check or not matches_file(file_name, check['ignore_files']):
                process = subprocess.Popen(check['command'] % file_name, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                out, err = process.communicate()
                if out or err:
                    if check['print_filename']:
                        prefix = '\t%s:' % file_name
                    else:
                        prefix = '\t'
                    output_lines = ['%s%s' % (prefix, line) for line in out.splitlines()]
                    print '\n'.join(output_lines)
                    if err:
                        print err
                    result = 1
    return result


def main(all_files):
    # Stash any changes to the working tree that are not going to be committed
    subprocess.call(['git', 'stash', '-u', '--keep-index'], stdout=subprocess.PIPE)
    
    files = []
    if all_files:
        for root, dirs, file_names in os.walk('.'):
            for file_name in file_names:
                files.append(os.path.join(root, file_name))
    else:
        p = subprocess.Popen(['git', 'status', '--porcelain'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            match = modified.match(line)
            if match:
                files.append(match.group('name'))
    
    result = 0
    
    for check in CHECKS:
        result = check_files(files, check) or result
    
    # Unstash changes to the working tree that we had stashed
    subprocess.call(['git', 'reset', '--hard'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.call(['git', 'stash', 'pop', '-q'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sys.exit(result)


if __name__ == '__main__':
    all_files = False
    if len(sys.argv) > 1 and sys.argv[1] == '--all-files':
        all_files = True
    main(all_files)
