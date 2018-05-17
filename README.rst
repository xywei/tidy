Tidy
====

**NOTE: Tidy is still in its pre-alpha (development) stage.**

Tidy is a document manager written in Python 3. The command line
interface for Tidy is `tid`. See `tid --help` for usage info.

Getting started
---------------

To start managing your documents, first create a __collection__.
A collection consists of a directory for all the files, an
`sqlite` database for the metadata, and a collection description
file `collection.json`.

To create an empty new collection, run
```bash
$ tid init CollectionName
```

Collections
-----------

Each collection is assigned a [UUID](https://tools.ietf.org/html/rfc4122.html)
(universally unique identifier).

## Adding files

Tidy manages documents added to it by putting them into the `Inbox`
and assigning a UUID for each file.

```bash
$ tid add [CollectionName] files
```

If no collection name is given, Tidy will put the files into the
global inbox at `$TIDY_HOME/Inbox`.

Configurations
--------------

Tidy can be customized through a configuration file at
`$XDG_CONFIG_HOME/tidy/config`, where `$XDG_CONFIG_HOME`
defaults to be `$HOME/.config`.

`$TIDY_HOME` defaults to be `$HOME/.tidy`.

Syncing
-------

It is not recommended that collections be synced directly with
cloud drives like Nextcloud or Dropbox unless you are comfortable
with resolving potential database conflicts manually.
