# coding: utf-8
# Copyright (c) Qotto, 2018-2019
# Open-source software, see LICENSE file for details

import doctest
import unittest

def load_tests(loader, tests, pattern):
    tests.addTests(doctest.DocTestSuite('smspdu.codecs'))
    tests.addTests(doctest.DocTestSuite('smspdu.elements'))
    tests.addTests(doctest.DocTestSuite('smspdu.fields'))
    return tests
