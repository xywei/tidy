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
from os import environ
import os.path

import tidy.config.files as config_files

def merge_dicts(*dict_args):
    """Shallow copy and merge dicts into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def load_json_config(filename):
    """Load a json config file.
    """
    with open(filename) as json_data_file:
        data = json.load(json_data_file)
    return data

if config_files.file_type == 'json':
    full_configs = [load_json_config(filename) for filename
            in config_files.file_list]
else:
    raise NotImplementedError

active_configs = merge_dicts(*full_configs)

# Postprocess for XDG base directories

if active_configs['use_default_data_dir']:
    """Where user-specific data files should be written.
    """
    if "XDG_DATA_HOME" in os.environ:
        active_configs['data_dir'] = os.path.expandvars('$XDG_DATA_HOME/tidy/')
    else:
        active_configs['data_dir'] = os.path.expanduser('~/.local/share/tidy/')
else:
    pass

if active_configs['use_default_cache_dir']:
    """Where user-specific non-essential (cached) data should be written.
    """
    if "XDG_CACHE_HOME" in os.environ:
        active_configs['cache_dir'] = os.path.expandvars('$XDG_CACHE_HOME/tidy/')
    else:
        active_configs['cache_dir'] = os.path.expanduser('~/.cache/tidy/')
else:
    pass

if active_configs['use_default_runtime_dir']:
    """Used for non-essential, user-specific data files such as sockets,
    named pipes, etc.
    """
    if "XDG_RUNTIME_DIR" in os.environ:
        active_configs['runtime_dir'] = os.path.expandvars('$XDG_RUNTIME_DIR/tidy/')
    else:
        active_configs['runtime_dir'] = os.path.expanduser('/tmp/tidy/')
