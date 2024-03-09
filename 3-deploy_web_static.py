#!/usr/bin/python3
# Distrubutes archive to the webservers
from fabric.api import env, put, run, sudo, local
from os.path import exists
from datetime import datetime


env.hosts = ['54.236.17.14', '18.209.223.91']
env.user = 'ubuntu'
env.key_file = '~/.ssh/id_rsa'


@task
def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        Path to the archive if successful, None otherwise.
    """
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
    """
    Distributes an archive to web servers and deploys it.

    Args:
        archive_path: Path to the archive file.

    Returns:
        True if successful, False otherwise.
    """
    if not exists(archive_path):
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


@task
def deploy():
    '''
    Deploys latest version of web_static code to the web servers
    
    Distributes an archive to web servers and deploys it.

    Args:
        archive_path: Path to the archive file.

    Returns:
        True if successful, False otherwise.
    
    '''
    archive_path = do_pack()

    if not archive_path:
        #print("Archive not created")
        return False

    return do_deploy(archive_path)
