#!/usr/bin/python3
'''
This is the '1-pack-web-static' module.

1-pack-web-static is a Fabric script that generates a .tgz archive from a given
location.

This module contains 1 function: do_pack().
'''
from fabric.api import *


def do_pack():
    '''This is the 'do_pack' function.
    do_pack generates a .tgz file and returns the archive path, or None.
    '''
    try:
        local("sudo mkdir -p versions/")
        local("sudo tar -zcvf\"./versions/web_static_`date +%Y%m%d%H%M%S`.tgz\"\
        web_static")
    except:
        return None
