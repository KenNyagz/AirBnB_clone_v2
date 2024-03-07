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
        archive_filename = archive_path.split("/")[-1]
        # Extract the filename without its extension for the release directory
        release_dir = "/data/web_static/releases/" + archive_filename.split(".")[0]
        
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(archive_filename))
        
        # Uncompress the archive to the folder on the web server
        run("mkdir -p {}".format(release_dir))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_dir))
        
        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))
        
        # Delete the symbolic link from the web server
        run("rm -rf /data/web_static/current")
        
        # Create a new the symbolic link on the web server
        run("ln -s {} /data/web_static/current".format(release_dir))

        print('Deployment successful')
        return True
    except Exception as e:
        print("Deployment failure:", e)
        return False
