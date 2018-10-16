from typing import Callable, Collection, Optional


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
