#!/usr/bin/python3
""" use fabric to generate and send info to server
"""
from fabric.operations import local, run, put
from datetime import datetime
from fabric.api import *
from os import path

env.hosts = ['35.229.126.169', '54.90.172.156']


def do_deploy(archive_path):
    """ script that distributes an archive to web servers
    """
    if not path.exists(archive_path):
        return False
    try:
        name_ext = archive_path.split("/")[-1]
        only_name = name_ext.split(".")[0]
        new_path = "/data/web_static/releases/" + only_name + "/"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_path))
        run("sudo tar -xzf /tmp/{} -C {}".format(name_ext, new_path))
        run("sudo rm /tmp/{}".format(name_ext))
        run("sudo mv {}web_static/* {}".format(new_path, new_path))
        run("sudo rm -rf {}web_static".format(new_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_path))
        print("New version deployed!")
        return True
    except Exception:
        return False
