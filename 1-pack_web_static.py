#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone
repo, using the function do_pack.
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """...
    """
    curr_time = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    outpt = local('tar -czvf versions/web-static_{}.tgz web_static'.
                  format(curr_time))

    if outpt.failed:
        return None
    else:
        return outpt
