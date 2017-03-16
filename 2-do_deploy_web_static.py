#!/usr/bin/python3
'''
This is the '2-do_deploy_web_static module.

2-do_deploy_web_static uses Fabric to distribute an archive to selected web
servers.

This module contains 1 function: do_deploy().
'''
from fabric.api import *

env.hosts = ['34.207.77.115', '54.208.161.26']


def do_deploy(archive_path):
    '''This is the do_deploy function.
    do_deploy has 1 parameter: the path to a given archive.
    The function distributes an archive to a web server, or returns False.
    '''
    try:
        # upload archive to /tmp directory of web server
        put(archive_path, "/tmp")
        path = archive_path.strip("versions/")
        s1 = "sudo mkdir -p /data/web_static/releases/" + path
        run(s1)

        # uncompress archive
        s2 = "sudo tar -xzf /tmp/" + path + " -C /data/web_static/releases/"
        s2 += path
        run(s2)

        # delete archive from web server
        run("rm /tmp/" + path)

        # delete symlink /data/web_server/current from web server
        s3 = "sudo mv /data/web_static/releases/" + path
        s3 += "/web_static/* /data/web_static/releases/" + path + "/"
        run(s3)
        s4 = "sudo rm -rf /data/web_static/releases/" + path + "/web_static"
        run(s4)
        run("sudo rm -rf /data/web_static/current")

        # create new symlink /data/web_server/current to new version of code
        s5 = "sudo ln -s /data/web_static/releases/" + path
        s5 += "/ /data/web_static/current"
        run(s5)
        return(True)

    except Exception as e:
        print(e)
        return(False)
