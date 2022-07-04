import unittest
from unittest.mock import patch

from mongoengine.errors import NotUniqueError

from connections.database import Database
from entities.holder import Holder
from services.holder import HolderService
from tests.fixtures.holder import VALID_HOLDER_DATA


class HolderServiceTest(unittest.TestCase):

    @patch.object(
        Database, 'save', return_value=Holder(**VALID_HOLDER_DATA)
    )
    def test_create_holder_successfully(self, save_mock):
        holder = HolderService().create_holder(
            data=VALID_HOLDER_DATA
        )
        self.assertIsNotNone(save_mock.called)
        self.assertEqual(holder.get('name'), VALID_HOLDER_DATA.get('name'))
        self.assertEqual(holder.get('tax_id'), VALID_HOLDER_DATA.get('tax_id'))

    @patch.object(
        Database, 'save', side_effect=NotUniqueError()
    )
    def test_create_holder_failure_not_unique(self, save_mock):
        with self.assertRaises(NotUniqueError):
            HolderService().create_holder(
                data=VALID_HOLDER_DATA
            )
            self.assertIsNotNone(save_mock.called)
