import unittest

from entities.holder import Holder
from tests.fixtures.holder import INVALID_TAX_ID_HOLDER_DATA, VALID_HOLDER_DATA


class HolderTest(unittest.TestCase):
    def test_valid_entity(self):
        holder = Holder(
            **VALID_HOLDER_DATA
        )
        holder.validate()
        self.assertEqual(
            holder.name,
            VALID_HOLDER_DATA.get('name').upper()
        )
        self.assertEqual(
            holder.tax_id,
            VALID_HOLDER_DATA.get('tax_id').upper()
        )

    def test_failure_invalid_tax_id(self):
        with self.assertRaises(Exception):
            holder = Holder(
                **INVALID_TAX_ID_HOLDER_DATA
            )
            holder.validate()
