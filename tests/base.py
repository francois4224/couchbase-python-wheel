# Copyright 2013, Couchbase, Inc.
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    from configparser import ConfigParser
except ImportError:
    # Python <3.0 fallback
    from ConfigParser import SafeConfigParser as ConfigParser
import os
import unittest


CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'tests.ini')


class CouchbaseTestCase(unittest.TestCase):
    def setUp(self):
        config = ConfigParser()
        config.read(CONFIG_FILE)

        self.host = config.get('node-1', 'host')
        self.port = config.getint('node-1', 'port')
        self.username = config.get('node-1', 'username')
        self.password = config.get('node-1', 'password')
        self.bucket_prefix = config.get('node-1', 'bucket_prefix')
        self.bucket_password = config.get('node-1', 'bucket_password')

    def tearDown(self):
        pass