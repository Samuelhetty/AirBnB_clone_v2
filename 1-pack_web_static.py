#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """generates a tgz archive"""
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    res = local("sudo tar -cvzf {} web_static".format(file_name))
    if res.succeeded:
        return file_name
    else:
        return None
