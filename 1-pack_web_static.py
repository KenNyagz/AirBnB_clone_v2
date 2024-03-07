from fabric.api import local
from datetime import datetime
import os

def do_pack():
    # Create the directory versions if it doesn't exist
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    
    # Format the current datetime to create a unique filename
    now = datetime.now()
    filename = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    
    # The full path of the archive to be created
    archive_path = "versions/{}".format(filename)
    
    # Command to tar and compress the contents of web_static
    command = "tar -cvzf {} web_static".format(archive_path)
    
    print("Packing web_static to {}".format(archive_path))
    # execute command
    result = local(command, capture=True)
    
    if result.failed:
        return None
    else:
        return archive_path
