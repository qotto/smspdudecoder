# Copyright (c) Qotto, 2018-2022
# Open-source software, see LICENSE file for details

import unittest

from smspdudecoder.elements import Number
from smspdudecoder.elements import TypeOfAddress


class NumberTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Number.encode(''), Number.decode(''), '')


class TypeOfAddressTestCase(unittest.TestCase):
    def test_unknown(self):
        self.assertEqual(TypeOfAddress.decode('80'), {'ton': 'unknown', 'npi': 'unknown'})
        self.assertEqual(TypeOfAddress.encode({'ton': 'unknown', 'npi': 'unknown'}), '80')

    def test_decode_invalid_extension(self):
        with self.assertRaises(ValueError):
            TypeOfAddress.decode('00')

    def test_decode_invalid_npi(self):
        with self.assertRaises(ValueError):
            TypeOfAddress.decode(f'{0x80|0b10:02x}')

    def test_encode_invalid_npi(self):
        with self.assertRaises(ValueError):
            TypeOfAddress.encode({'npi': 'strange', 'ton': 'international'})

    def test_encode_invalid_ton(self):
        with self.assertRaises(ValueError):
            TypeOfAddress.encode({'npi': 'isdn', 'ton': 'strange'})

    def test_encode_invalid_dict(self):
        with self.assertRaises(ValueError):
            TypeOfAddress.encode({})
