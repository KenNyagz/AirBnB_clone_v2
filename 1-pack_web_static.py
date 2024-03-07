#!/usr/bin/python3
'''fabfile generates .tgz ar from web_static/'s contents'''
from fabric.api import local
from datetime import datetime


def do_pack:
    '''return archive path of archive created from web_static contents'''
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
