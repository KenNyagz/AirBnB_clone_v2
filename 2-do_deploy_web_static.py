#!/usr/bin/python3
# Distrubutes archive to the webservers
from fabric.api import env, put, run, sudo, local, task
from os.path import exists
from datetime import datetime


env.hosts = ['54.236.17.14', '18.209.223.91']
env.user = 'ubuntu'
env.key_file = '~/.ssh/id_rsa'


@task
def do_pack():
    '''
    return archive path of archive created from web_static contents
    '''
    try:
        local("mkdir -p versions")

        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)

        # Create the .tgz archive
        local("tar -czvf versions/{} web_static".format(archive_name))

        return "versions/{}".format(archive_name)
    except Exception as e:
        print("Couldn't create archive")
        return None


@task
def do_deploy(archive_path):
    '''
    deploys static content to web servers
    '''
    if not exists:
        return False

    try:
        put(archive_path, '/tmp/')

        archive_filename = archive_path.split('/')[-1]
        archive_name = archive_filename.split('.')[0]
        release_path = '/data/web_static/releases/{}/'.format(archive_name)
        sudo('mkdir -p {}'.format(release_path))
        sudo('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))
        sudo('mv /data/web_static/releases/{}/web_static/*\
 /data/web_static/releases/{}/'.format(archive_name, archive_name))
        sudo('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_name))

        # Delete archive from archive
        sudo('rm /tmp/{}'.format(archive_filename))

        # Delete existing symbolic link
        sudo('rm -rf /data/web_static/current')
        # new symbolic link
        sudo('ln -s {} /data/web_static/current'.format(release_path))

        print('Deployment successful')
        return True
    except Exception as e:
        print("Deployment failure:", e)
        return False
