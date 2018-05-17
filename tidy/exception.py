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


class TidyErrorBase(Exception):
    """Bass class for exceptions in Tidy.
    """


class TidyCollectionDirectoryStructureError(TidyErrorBase):
    """Raised when the assumptions on collection directory structures
    are not satisfied.

    Attributes:
        directory -- the problematic directory
        message -- explanation of why the directory structure is broken
    """

    def __init__(self, directory, message):
        self.directory = directory
        self.message = message


class TidyCollectionLockError(TidyErrorBase):
    """Raised when trying to access a locked collection.
    When accessing a collection, Tidy puts a access.lock in the collection
    directory with its pid info to ensure that only one process can open the
    collection at a time.

    Attributes:
        directory -- the problematic directory
        lock_info -- the content of access.lock
    """

    def __init__(self, directory, lock_info):
        self.directory = directory
        self.lock_info = lock_info


class TidyCollectionLockCorruptionError(TidyErrorBase):
    """Raised when the information in access.lock smells bad.

    Attributes:
        directory -- the problematic directory
        message -- explanation of why Tidy thinks that the lock has gone bad
    """

    def __init__(self, directory, message):
        self.directory = directory
        self.message = message
