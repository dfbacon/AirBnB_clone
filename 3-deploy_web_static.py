#!/usr/bin/python3
'''
This is the '3-deploy_web_static' module.
'''
from fabric.api import run, put, env, local
from fabric.decorators import runs_once
from datetime import datetime
import os

env.hosts = ['34.207.77.115', '54.208.161.26']


@runs_once
def do_pack():
    '''This is the 'do_pack' function.
    do_pack generates a .tgz file and returns the archive path, or None.
    '''
    local("sudo mkdir -p versions")
    tar_1 = "tar czfv web_static_"
    tar_2 = datetime.now().__format__("%Y%m%d%H%M%S")
    tar_3 = ".tgz web_static"
    local(tar_1 + tar_2 + tar_3)
    archive_name = "web_static_" + tar_2 + ".tgz"
    new_name = "./versions/" + archive_name
    try:
        local("sudo mv " + archive_name + " " + new_name)
    except:
        return(None)
    return("./versions/" + archive_name)


def do_deploy(archive_path):
    '''This is the do_deploy function.
    do_deploy has 1 parameter: the path to a given archive.
    The function distributes an archive to a web server, or returns False.
    '''
    try:
        put(archive_path, "/tmp/")
        a, b = archive_path.find("web_static_"), archive_path.find(".tgz")
        filename = archive_path[a:b]
        make_dir = "sudo mkdir -p /data/web_static/releases/" + filename
        run(make_dir)
        tar = "sudo tar -xzf /tmp/" + filename + ".tgz -C "
        tar = tar + "/data/web_static/releases/" + filename + "/"
        run(tar)
        run("sudo rm /tmp/" + filename + ".tgz")
        run("sudo rm -rf /data/web_static/current")
        name_a = "sudo mv /data/web_static/releases/" + filename
        name_b = "/web_static/* /data/web_static/releases/" + filename + "/"
        run(name_a + name_b)
        link_a = "sudo ln -s /data/web_static/releases/" + filename + "/"
        link_b = " /data/web_static/current"
        run(link_a + link_b)
        return(True)
    except:
        return(False)


def deploy():
    '''This is the deploy function.
    '''
    archive_path = do_pack()
    if archive_path is None:
        return(False)
    return(do_deploy(archive_path))
