# coding: utf-8

from fabkit import filer
from fablib.base import SimpleBase


class Memcached(SimpleBase):
    def __init__(self):
        self.data_key = 'memcached'
        self.data = {}

        self.services = {
            'CentOS Linux 7.*': [
                'memcached',
            ],
        }

        self.packages = {
            'CentOS Linux 7.*': [
                'memcached',
            ],
        }

    def setup(self):
        data = self.init()

        if self.is_tag('package'):
            self.install_packages()

        if self.is_tag('conf'):
            if filer.template('/etc/sysconfig/memcached', data=data):
                self.handlers['restart_memcached'] = True

        if self.is_tag('service'):
            self.enable_services().start_services()
            self.exec_handlers()
