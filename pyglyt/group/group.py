import itertools
from typing import Any, Callable, Collection, Generator, Optional


class Group:
    """Class implementing an algebraic group"""

    def __init__(
        self,
        generators: Collection,
        operation: Callable,
        identity: Optional = None,
    ) -> None:
        self.generators = set(generators)
        self.operation = operation
        self.identity = identity

    def __repr__(self) -> str:
        """Repr string for group class"""
        return (
            f"{self.__class__.__name__}("
            f"generators={self.generators!r}, "
            f"operation={self.operation!r})"
        )

    def _powers(
        self, element: Any, inverse: Optional[Any] = None
    ) -> Generator:
        """Return an iterator over powers of `element`"""
        powers = itertools.accumulate(
            itertools.repeat(element), self.operation
        )

        if inverse is not None:
            neg_powers = itertools.accumulate(
                itertools.repeat(inverse), self.operation
            )
            powers = itertools.chain.from_iterable(zip(powers, neg_powers))
            identity = self.operation(element, inverse)
            powers = itertools.chain((identity,), powers)
            yield next(powers)  # Yield identity

        yield next(powers)  # Yield `element`
        for g in powers:
            if g == element:
                break
            yield g
