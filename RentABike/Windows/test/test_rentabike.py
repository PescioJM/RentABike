# -*- coding: utf-8 -*-
#!/usr/bin/env python

# metadata:
__author__ = "Juan Manuel Pescio"
__email__ = "juanmp012@gmail.com"

import unittest
import time
import rentabike

class TestRent(unittest.TestCase):

    def test_main(self):
        result = rentabike.Rent(3,'2',3,False).rent_cost()
        self.assertAlmostEqual(result,126.0)

if __name__ == "__main__":
    unittest.main()
