from .menuitems import DashboardMenuItem
from .registry import DashboardPluginRegistry


def initialize(supervisor):
    supervisor.exts.dashboard = DashboardPluginRegistry()
    supervisor.exts.menuitems.register(DashboardMenuItem)


def init_complete(supervisor):
    plugin_list = supervisor.config['dashboard.plugins']
    supervisor.exts.dashboard.sort(plugin_list)
