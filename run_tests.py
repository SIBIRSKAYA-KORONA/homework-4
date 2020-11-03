# -*- coding: utf-8 -*-

import unittest
import sys

if __name__ == '__main__':
    loader = unittest.TestLoader()
    cases = sys.argv[1] if len(sys.argv) == 2  else './cases'
    suite = loader.discover(cases)

    runner = unittest.TextTestRunner()
    runner.run(suite)
