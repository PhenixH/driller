from distutils.core import setup
import subprocess


setup(
        name='driller',
        version='1.0',
        packages=['driller'],
        data_files=[
            ('bin/driller', ('bin/driller/listen.py',),),
        ],
        install_requires=[
            'cle',
            'angr',
            'redis',
            'celery',
            'simuvex',
            'archinfo',
            'dpkt-fix',
            'termcolor',
        ],
)
