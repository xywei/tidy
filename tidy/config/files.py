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

import os.path
from os import environ

file_type = 'json'

# Latter ones overwrite ealier ones
file_list = [os.path.realpath(__file__)[:-8] + 'default_config.json', ]

if "XDG_CONFIG_HOME" in os.environ:
    user_config_file = os.path.expandvars('$XDG_CONFIG/tidy/config.json')
else:
    user_config_file = os.path.expanduser('~/.config/tidy/config.json')

file_list.append(user_config_file)
