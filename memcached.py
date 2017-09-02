# coding: utf-8

import re
from fabkit import filer, env
from fablib.base import SimpleBase

RE_CENTOS = re.compile('CentOS .*')
RE_UBUNTU = re.compile('Ubuntu .*')


class Memcached(SimpleBase):
    def __init__(self):
        self.data_key = 'memcached'
        self.data = {}

        self.services = {
            'CentOS .*': [
                'memcached',
            ],
            'Ubuntu .*': [
                'memcached',
            ],
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
            self.install_packages()

        if self.is_tag('conf'):
            if RE_CENTOS.match(env.node['os']):
                if filer.template('/etc/sysconfig/memcached', data=data):
                    self.handlers['restart_memcached'] = True
            elif RE_UBUNTU.match(env.node['os']):
                if filer.template('/etc/memcached.conf', data=data):
                    self.handlers['restart_memcached'] = True

        if self.is_tag('service'):
            self.enable_services().start_services()
            self.exec_handlers()
