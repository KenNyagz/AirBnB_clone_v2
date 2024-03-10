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
    try:
        local('ls -t versions | tail -n +{} | xargs -I {{}} rm versions/{{}}'
              .format(number + 1))
        for host in env.hosts:
            releases = run("ls -t /data/web_static/releases".split())
            for releases in releases[numbers:]:
                sudo("rm -rf /data/web_static/releases/{}".format(releases))
    except Exception as e:
        print("Error")
