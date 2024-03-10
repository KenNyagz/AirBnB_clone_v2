#!/usr/bin/python3
# Clean unwanted archives from the server
from fabric.api import env, run, local
from fabric.operations import sudo
from datetime import datetime


env.hosts = ['54.236.17.14', '18.209.223.91']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    '''Deletes unused archive from the server'''
    number = int(number)
    if number < 2:
        number = 1
    try:
        # Delete unnecessary archives in the versions folder
        with lcd('versions'):
            local("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))
        # Del unnecessary archives in /data/web_static/releases dir on server
        with cd('/data/web_static/releases'):
            sudo("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))
        return True
    except Exception as e:
        print("Error")
        return False
