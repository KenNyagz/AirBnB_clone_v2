#!/usr/bin/python3

archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)
tar -czvf versions/archive_name web_static
