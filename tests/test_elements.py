# coding: utf-8
# Copyright (c) Qotto, 2018

import unittest

from datetime import datetime, timezone, timedelta
from smspdu.elements import Date
from smspdu.elements import Number
from smspdu.elements import TypeOfAddress

class DateTestCase(unittest.TestCase):
    def test_gmt(self):
        d1 = Date.decode('11101131521400')
        d2 = datetime(2011, 1, 11, 13, 25, 41, tzinfo=timezone.utc)
        self.assertEqual(d1, d2, '')

    def test_gmt_plus_3(self):
        d1 = Date.decode('111011315214C0')
        d2 = datetime(2011, 1, 11, 13, 25, 41, tzinfo=timezone(timedelta(hours=3)))
        self.assertEqual(d1, d2, '')

    def test_gmt_minus_10(self):
        d1 = Date.decode('1110113152140C')
        d2 = datetime(2011, 1, 11, 13, 25, 41, tzinfo=timezone(timedelta(hours=-10)))
        self.assertEqual(d1, d2, '')

    def test_decode(self):
        dates1 = []
        dates2 = []
        for hour in range(-13, 13):
            if hour < 0:
                quarter = int(f'{-4 * hour:02d}', 16) + 128
            else:
                quarter = 4 * hour
            quarter = f'{quarter:02X}'[::-1]
            dates1.append(Date.decode('111011315214%s' % quarter))
            dates2.append(datetime(2011, 1, 11, 13, 25, 41,
                                   tzinfo=timezone(timedelta(hours=hour))))
        self.assertEqual(dates1, dates2, '')

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
