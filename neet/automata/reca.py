# Copyright 2017 ELIFE. All rights reserved.
# Use of this source code is governed by a MIT
# license that can be found in the LICENSE file.
from neet.landscape import StateSpace
from . import eca

class RewiredECA(eca.ECA):
    """
    RewiredECA is a class to represent elementary cellular automata rules with
    arbitrarily defined topology. Since the topology must be provided,
    RewiredECA are naturally fixed-sized.
    """
    def __init__(self, code, boundary=None, size=None, wiring=None):
        """
        Construct a rewired elementary cellular automaton rule.

        :param code: the 8-bit Wolfram code for the rule
        :type code: int
        :param boundary: the boundary conditions for the CA
        :type boundary: tuple or None
        :param size: the number of cells in the lattice
        :type size: int or None
        :param wiring: a wiring matrix
        :raises ValueError: if `size is None and wiring is None`
        :raises ValueError: if `size is not None and wiring is not None`
        :raises TypeError: if `size is not None and not isinstance(size, int)`
        :raises ValueError: if `size is not None and size <= 0`
        """
        super(RewiredECA, self).__init__(code, boundary=boundary)
        if size is not None and wiring is not None:
            raise ValueError("cannot provide size and wiring at the same time")
        elif size is not None:
            if not isinstance(size, int):
                raise TypeError("size must be an int")
            elif size <= 0:
                raise ValueError("size must be positive, nonzero")
            else:
                self.__size = size
                self.__wiring = None
        elif wiring is not None:
            self.__size = None
            self.__wiring = wiring
        else:
            raise ValueError("either size or wiring must be provided")

    @property
    def size(self):
        """
        The number of cells in the CA lattice.

        :type: int
        """
        return self.__size

    def state_space(self):
        """
        Return a :class:`StateSpace` object for the cellular automaton lattice.

        :returns: :class:`StateSpace`
        """
        return StateSpace(self.__size, b=2)
