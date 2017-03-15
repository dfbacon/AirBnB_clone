#!/usr/bin/python3
'''
This is the '2-do_deploy_web_static module.

2-do_deploy_web_static uses Fabric to distribute an archive to selected web
servers.

This module contains 1 function: do_deploy().
'''
from fabric.api import *
import sys

env.hosts = ['34.207.77.115', '54.208.161.26']
env.user = sys.argv[7]
env.password = sys.argv[5]


def do_deploy(archive_path):
    '''This is the do_deploy function.
    do_deploy has 1 parameter: the path to a given archive.
    The function distributes an archive to a web server, or returns False.
    '''
    try:
        # upload archive to /tmp directory of web server
        put(archive_path, "/tmp")
        # uncompress to /data/web_static/releases/<archive filename without extension>

        # delete archive from web server

        # delete symlink /data/web_server/current from web server

        # create new symlink /data/web_server/current to new version of code
        # /data/web_static/releases/<archive filename without extension>

        return(True)
    except Exception as e:
        print(e)
        return(False)
