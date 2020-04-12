#!/usr/bin/python3
""" use fabric to generate and send info to server
"""
from fabric.operations import local, run, put
from datetime import datetime
from fabric.api import env
from os import path
env.user = 'ubuntu'
env.hosts = [
    '35.229.126.169',
    '54.90.172.156',
]


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


def do_deploy(archive_path):
    """ script that distributes an archive to web servers
    """
    if not path.exists(archive_path):
        return False
    try:
        name_ext = archive_path.split("/")
        only_name = name_ext[-1].split(".")
        new_path = "/data/web_static/releases/" + only_name[0]
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_path))
        run("sudo tar -xzf /tmp/{} -C {}".format(name_ext[-1], new_path))
        run("sudo rm /tmp/{}".format(name_ext[1]))
        run("sudo mv {}/web_static/* {}/".format(new_path, new_path))
        run("sudo rm -rf {}/web_static".format(new_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} /data/web_static/current".format(new_path))
        return True
    except Exception:
        return False
