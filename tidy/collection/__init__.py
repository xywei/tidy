__copyright__ = "Copyright (C) 2018 Xiaoyu Wei"

__license__ = """
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import json
import os
import os.path
import sqlite3
from tidy.exception import \
        TidyCollectionDirectoryStructureError, \
        TidyCollectionLockError

# {{{ preload checks

def preload_checks(*, collection_path, lock_path, info_path, db_path, data_dir,
        clone_dir):
    """Quick checks performed before loading a collection, just to
    gain some confidence that it is indeed a collection path.
    """
    passed = False

    if not os.path.isdir(collection_path):
        why = "invalid collection path"
        raise TidyCollectionDirectoryStructureError(
                collection_path, why)

    elif not os.path.isfile(info_path):
        why = "missing collection.json"
        raise TidyCollectionDirectoryStructureError(
                collection_path, why)

    elif not os.path.isfile(db_path):
        why = "missing sqlite database"
        raise TidyCollectionDirectoryStructureError(
                collection_path, why)

    elif not os.path.isdir(data_dir)
        why = "missing data directory"
        raise TidyCollectionDirectoryStructureError(
                collection_path, why)

    elif os.path.isfile(lock_path):
        with lock_file = open(collection_path + '/access.lock'):
            lock_info = lock_file.read()
        raise TidyCollectionLockError(collection_path, lock_info)

    else:
        passed = True

    return passed

# }}} End preload checks

class Collection(object):
    """Collection class.
    """
    def __init__(self, collection_path):
        """Constructor.
        """
        self.collection_path = collection_path
        self.lock_path = collection_path + '/access.lock'
        self.info_path = collection_path + '/collection.json'
        self.db_path   = collection_path + '/meta.sqlite'
        self.data_dir  = collection_path + '/data/'
        self.clone_dir = collection_path + '/clones/'

        preload_checks(collection_path=self.collection_path,
                lock_path=self.lock_path,
                info_path=self.info_path,
                db_path=self.db_path,
                data_dir=self.data_dir,
                clone_dir=self.clone_dir)

    def lock_dir(self):
        """Create access.lock
        """
        # access.locks, if exists, should not have passed preload_checks()
        assert not os.path.isfile(self.lock_path)

        pid = os.getpid()
        with open(self.lock_path, 'w') as lock:
            lock.write(str(pid))

    def unlock_dir(self):
        """Remove access.lock
        """
        assert os.path.isfile(self.lock_path)
        with open(self.lock_path, 'r') as lock:
            lock_pid = lock.read()
        pid = os.getpid()
        if not str(pid)==lock_pid:
            raise TidyCollectionLockCorruptionError(
                    self.collection_path,
                    "trying to unlock a lock that was set by a "
                    "different process (I am " + str(pid) + ", "
                    "but the lock is " + lock_pid + ")")
        else:
            os.remove(self.lock_path)

    def __enter__(self):
        """Auto-lock using `with` statement.
        """
        self.lock_dir()
        self.db_connection = sqlite3.connect(self.db_path)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Auto-unlock using `with` statement.
        """
        self.db_connection.close()
        self.unlock_dir()

    def connect(self, collection_name):
        pass


# vim: fdm=marker
