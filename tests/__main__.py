# Copyright (c) Qotto, 2018-2023
# Open-source software, see LICENSE file for details

import os
import unittest

def load_tests(loader, tests, pattern):
    test_dir = os.path.dirname(__file__)
    top_dir = os.path.dirname(test_dir)
    package_tests = loader.discover(start_dir=test_dir, pattern='test_*.py', top_level_dir=top_dir)
    tests.addTests(package_tests)
    return tests

if __name__ == '__main__':
    unittest.main()
