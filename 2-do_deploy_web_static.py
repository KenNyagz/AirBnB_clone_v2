#!/usr/bin/python3
# Distrubutesarchive to the webservers
from fabric.api import env, put, run, sudo
# from os.path import exists
import os
from datetime import datetime


env.hosts = ['54.236.17.14']
env.user = 'ubuntu'
env.key_file = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    '''deploys static content to web servers'''
    if not exists:
        return False

    try:
        put(archive_path, "/tmp/")

        # Uncompress the archive to the /data/web_static/releases/ directory on the web server
        archive_filename = os.path.basename(archive_path)
        archive_folder = "/data/web_static/releases/{}".format(os.path.splitext(archive_filename)[0])
        run("mkdir -p {}".format(archive_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, archive_folder))
        run("rm /tmp/{}".format(archive_filename))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current on the web server
        run("ln -s {} /data/web_static/current".format(archive_folder))

        print('Deployment successful')
        return True
    except Exception as e:
        print("Deployment failure:", e)
        return False
