"""
plugins: code related to plugins and plugin loaders

Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

import logging


class DashboardPluginRegistry(object):

    def __init__(self):
        self.collected = dict()
        self.installed = []

    def register(self, plugin_cls):
        self.collected[plugin_cls.name] = plugin_cls

    def sort(self):
        # Install dashboard plugins for plugins that have them
        self.installed = [i[1]() for i in sorted(self.collected.items(),
                                               key=lambda c: c[1].priority,
                                               reverse=True)]

    @property
    def plugins(self):
        return self.installed
