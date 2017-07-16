# coding: utf-8

from fabkit import task
from fablib.memcached import Memcached


@task
def setup():
    memcached = Memcached()
    memcached.setup()
