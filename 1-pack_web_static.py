#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from
    the contents of the web_static
"""
from fabric.operations import local
from datetime import datetime


def do_pack():
    """archive from the contents of the web_static folder
    using do_pack function
    """
    local("mkdir -p versions")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(
            datetime.now().strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{}.tgz web_static/".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))
    except Exception:
        return None
