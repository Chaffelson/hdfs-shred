#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Configuration parameters for Shred client and server processors"""

VERSION = "0.0.1"


PATHS = {
    'HDFS_APP_ROOT': '/apps/shred',
    'HDFS_LOG_ROOT': '/app-logs/shred'
}

ZOOKEEPER = {
    'HOST': 'localhost',
    'PORT': 2181
}

HDFS = {
    'KEYTAB': '/etc/security/keytabs/hdfs.headless.keytab'
}