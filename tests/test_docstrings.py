# Copyright (c) Qotto, 2018-2022
# Open-source software, see LICENSE file for details

import doctest


def load_tests(loader, tests, pattern):
    tests.addTests(doctest.DocTestSuite('smspdudecoder.codecs'))
    tests.addTests(doctest.DocTestSuite('smspdudecoder.elements'))
    tests.addTests(doctest.DocTestSuite('smspdudecoder.fields'))
    return tests
