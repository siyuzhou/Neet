# Copyright 2017 ELIFE. All rights reserved.
# Use of this source code is governed by a MIT
# license that can be found in the LICENSE file.
import unittest
from neet.automata.reca import RewiredECA

class TestRewiredECA(unittest.TestCase):
    """
    Unit tests of the RewiredECA class
    """
    def test_is_network(self):
        """
        Ensure that RewiredECA meets the requirement of a network
        """
        from neet.interfaces import is_network
        self.assertTrue(is_network(RewiredECA))
        self.assertTrue(is_network(RewiredECA(23, size=3)))
        self.assertTrue(is_network(RewiredECA(30, wiring=[[-1, 0, 1], [0, 1, 2], [1, 2, 0]])))


    def test_is_fixed_sized(self):
        """
        Ensure that RewiredECA is of fixed size
        """
        from neet.interfaces import is_fixed_sized
        self.assertTrue(is_fixed_sized(RewiredECA))
        self.assertTrue(is_fixed_sized(RewiredECA(23, size=3)))
        self.assertTrue(is_fixed_sized(RewiredECA(30, wiring=[[-1, 0, 1], [0, 1, 2], [1, 2, 0]])))


    def test_invalid_code(self):
        """
        Ensure that init fails when an invalid Wolfram code is provided
        """
        with self.assertRaises(ValueError):
            RewiredECA(-1, size=3)
        with self.assertRaises(ValueError):
            RewiredECA(256, size=3)
        with self.assertRaises(TypeError):
            RewiredECA("30", size=3)


    def test_invalid_boundary(self):
        """
        Ensure that init fails when an invalid boundary condition is provided
        """
        with self.assertRaises(TypeError):
            RewiredECA(30, boundary=[1, 2], size=3)
        with self.assertRaises(ValueError):
            RewiredECA(30, boundary=(1, 0, 1), size=3)
        with self.assertRaises(ValueError):
            RewiredECA(30, boundary=(1, 2), size=3)


    def test_invalid_size(self):
        """
        Ensure that init fails when an invalid size is provided
        """
        with self.assertRaises(TypeError):
            RewiredECA(30, size="3")
        with self.assertRaises(ValueError):
            RewiredECA(30, size=-1)
        with self.assertRaises(ValueError):
            RewiredECA(30, size=0)


    def test_invalid_size_wiring(self):
        """
        Ensure that size and wiring are not both provided, but at least one is
        """
        with self.assertRaises(ValueError):
            RewiredECA(30, size=3, wiring=[])
        with self.assertRaises(ValueError):
            RewiredECA(30)
        with self.assertRaises(ValueError):
            RewiredECA(30, boundary=(0, 0))
