Tidy
====

**NOTE: Tidy is still in its pre-alpha (development) stage.**

Tidy is a document manager written in Python 3. The command line
interface for Tidy is `tid`. See `tid --help` for usage info.

Getting started
---------------

To start managing your documents, first create a **collection**.
A collection consists of a directory for all the files, an
``sqlite`` database for the metadata, and a collection description
file ``collection.json``.

Collections
-----------

Each collection is assigned a UUID_
(universally unique identifier).

.. _UUID: https://tools.ietf.org/html/rfc4122.html

## Adding files

Tidy manages documents added to it by putting them into the `Inbox`
and assigning a UUID for each file.

Configurations
--------------

Tidy can be customized through a configuration file at
``$XDG_CONFIG_HOME/tidy/config``, where ``$XDG_CONFIG_HOME``
defaults to be ``$HOME/.config``.

``$TIDY_HOME`` defaults to be ``$HOME/.tidy``.

Syncing
-------

It is not recommended that collections be synced directly with
cloud drives like Nextcloud or Dropbox unless you are comfortable
with resolving potential database conflicts manually.

Documentation
-------------

The documentation can be browsed here_.

.. _here: https://tidy.readthedocs.io
