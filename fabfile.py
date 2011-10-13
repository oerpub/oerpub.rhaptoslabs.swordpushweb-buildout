"""
Fabric script for deploying the word converter consistently.
"""

from __future__ import with_statement
from fabric.api import env, cd, run

def qa():
    """
    Set the context to the QA server
    """
    env.hosts = ['oerpub@swordpush.404.co.za']
    env.directory = '/var/www/swordpushweb'

def _with_deploy_env(commands=[]):
    """
    Run a set of commands.
    """
    with cd(env.directory):
        for command in commands:
            run(command)

def pull():
    """
    Do a git pull.
    """
    _with_deploy_env(['git pull'])

def dev_up():
    """
    Update all the mr developer packages
    """
    _with_deploy_env(['./bin/develop up'])

def stop():
    """
    Shutdown the pyramid app.
    """
    _with_deploy_env(['./bin/paster serve src/oerpub.rhaptoslabs.swordpushweb/oerpub/rhaptoslabs/production.ini --stop-daemon'])
        
def start():
    """
    Start up the pyramid app.
    """
    _with_deploy_env(['./bin/paster serve src/oerpub.rhaptoslabs.swordpushweb/oerpub/rhaptoslabs/production.ini --daemon'])

def restart():
    """
    Restart just the zope instance, not the zeo.
    """
    stop()
    start()

def status():
    """
    Find out the running status of the server and deploy.
    """

    # General health of the server.
    run('cat /proc/loadavg')
    run('uptime')
    run('free')
    run('df -h')

    # Get an overview of the packages
    print '================================== Buildout'
    _with_deploy_env(['./bin/develop status',
                      'git status',
                      'git log -1'])

    git_packages = ['oerpub.rhaptoslabs.cnxml2htmlpreview',
                    'oerpub.rhaptoslabs.sword1cnx',
                    'oerpub.rhaptoslabs.sword2cnx',
                    'oerpub.rhaptoslabs.swordpushweb',
                    'rhaptos.cnxmlutils',
                    ]

    for package in git_packages:
        print '================================== %s' % package
        with cd('%s/src/%s' % (env.directory, package)):
            run('git status')
            run('git log -1')

def buildout():
    """
    Rerun buildout.
    """
    _with_deploy_env(['./bin/buildout -Nvv'])
