#!/usr/bin/python3
from datetime import datetime
import subprocess

now = datetime.now()
archive_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

subprocess.run(['tar', '-czvf', archive_name, '../web_static'])
