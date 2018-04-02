# fablib memcached


## Overview
This is memcached of fablib.


## Running test-repo
```
$ fab test:l=memcached,c=ubuntu16,p='bootstrap|setup'
```


## Testing Guidelines
```
$ tox
...
Done.
Disconnecting from memcached-ubuntu16-1.example.com... done.
Disconnecting from memcached-centos7-1.example.com... done.
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
__init__.py        1      0   100%
memcached.py      22      0   100%
--------------------------------------------
TOTAL             23      0   100%
```


## License
This is licensed under the MIT. See the [LICENSE](./LICENSE) file for details.
