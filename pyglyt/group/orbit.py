import itertools
import functools
from typing import Any, Callable, Optional

from .group import Group
from .. import constants


class Orbit:
    """Orbit class"""

    def __init__(
        self,
        group: Group,
        element: Any,
        action: Callable,
        cache: Optional[bool] = None,
    ) -> None:
        self.group = group
        self.element = element
        self.action = action
        self._elements = []
        if cache is not None:
            self._cache = cache
        else:
            self._cache = constants.CACHE

    def __iter__(self):
        """Return an iterator over elements of the orbit.

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
                    self._elements.append(y)
                    yield y
            if not self._cache:
                self._elements = []
