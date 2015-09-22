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

    def sort(self, by_names):
        # Install dashboard plugins for plugins that have them
        logging.debug("Installing dashboard plugins: %s", ', '.join(by_names))
        for name in by_names:
            if name not in self.collected:
                logging.debug("Plugin '%s' is not installed, ignoring", name)
                continue
            plugin_cls = self.collected[name]
            try:
                self.installed.append(plugin_cls())
                logging.info('Installed dashboard plugin %s', name)
            except AttributeError:
                logging.debug("No dashboard plugin for '%s'", name)
                continue

    @property
    def plugins(self):
        return self.installed
