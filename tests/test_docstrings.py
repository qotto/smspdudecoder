import doctest
import unittest

def load_tests(loader, tests, pattern):
    tests.addTests(doctest.DocTestSuite('smspdu.codecs'))
    return tests
