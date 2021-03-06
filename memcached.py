# coding: utf-8

from fabkit import filer, env
from fablib.base import SimpleBase


class Memcached(SimpleBase):
    def __init__(self):
        self.data_key = 'memcached'
        self.data = {}

        self.services = {
            'CentOS .*': [
                'memcached',
            ],
            'Ubuntu .*': [
                'memcached'
            ]
        }

        self.packages = {
            'CentOS .*': [
                'memcached',
            ],
            'Ubuntu .*': [
                'memcached',
            ],
        }

    def setup(self):
        data = self.init()

        if self.is_tag('package'):
            self.init_package_manager()
            self.install_packages()

        if self.is_tag('conf'):
            if env.node['package_manager'] == 'apt':
                if filer.template('/etc/memcached.conf', data=data):
                    self.handlers['restart_memcached'] = True
            else:
                if filer.template('/etc/sysconfig/memcached', data=data):
                    self.handlers['restart_memcached'] = True

        if self.is_tag('service'):
            self.enable_services().start_services()
            self.exec_handlers()
