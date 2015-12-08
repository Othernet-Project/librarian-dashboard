===================
librarian-dashboard
===================

Base component providing facilities to create and register dashboard plugins.

Installation
------------

The component has the following dependencies:

- librarian-core_
- librarian-menu_
- librarian-auth_

To enable this component, add it to the list of components in librarian_'s
`config.ini` file, e.g.::

    [app]
    +components =
        librarian_dashboard

Development
-----------

In order to recompile static assets, make sure that compass_ and coffeescript_
are installed on your system. To perform a one-time recompilation, execute::

    make recompile

To enable the filesystem watcher and perform automatic recompilation on changes,
use::

    make watch

.. _librarian: https://github.com/Outernet-Project/librarian
.. _librarian-core: https://github.com/Outernet-Project/librarian-core
.. _librarian-menu: https://github.com/Outernet-Project/librarian-menu
.. _librarian-auth: https://github.com/Outernet-Project/librarian-auth
.. _compass: http://compass-style.org/
.. _coffeescript: http://coffeescript.org/
