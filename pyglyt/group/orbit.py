import itertools
import functools
from typing import Any, Callable

from .group import Group
from ..constants import CACHE


class Orbit:
    """Orbit class"""

    def __init__(
        self, group: Group, element: Any, action: Callable, cache: bool = CACHE
    ) -> None:
        self.group = group
        self.element = element
        self.action = action
        self._cache = cache
        if cache:
            self._elements = []

    def __iter__(self):
        """Return an iterator over element of the orbit.

        Warning: This may cause an infinite loop for infinite groups.
        """
        if self._cache and self._elements:
            for element in self._elements:
                yield element
        else:
            self._elements.append(self.element)
            yield self.element
            _powers = self.group._powers
            _generators = self.group.generators
            # NOTE: Below line blows up for infinite cyclic groups
            powers_of_generators = tuple(_powers(g) for g in _generators)
            for g in itertools.product(*powers_of_generators):
                # NOTE: functools.reduce blows up for generators that
                # generate an infinite cyclic subgroup
                x = functools.reduce(self.group.operation, g)
                y = self.action(self.element, x)
                if y not in self._elements:
                    if self._cache:
                        self._elements.append(y)
                    yield y
