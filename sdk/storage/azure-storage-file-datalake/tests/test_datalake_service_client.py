# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import unittest
from datetime import datetime, timedelta

from azure.core.exceptions import ResourceNotFoundError

from azure.core import MatchConditions

from azure.storage.filedatalake import DataLakeServiceClient, PublicAccess
from testcase import (
    StorageTestCase,
    record,
)

# ------------------------------------------------------------------------------
from azure.storage.filedatalake import AccessPolicy, FileSystemSasPermissions

TEST_FILE_SYSTEM_PREFIX = 'filesystem'
# ------------------------------------------------------------------------------


class FileSystemTest(StorageTestCase):
    def setUp(self):
        super(FileSystemTest, self).setUp()
        url = self._get_account_url()
        self.dsc = DataLakeServiceClient(url, credential=self.settings.STORAGE_DATA_LAKE_ACCOUNT_KEY)
        self.config = self.dsc._config
        self.test_file_systems = []

    def tearDown(self):
        if not self.is_playback():
            try:
                for file_system in self.test_file_systems:
                    self.dsc.delete_file_system(file_system)
            except:
                pass

        return super(FileSystemTest, self).tearDown()