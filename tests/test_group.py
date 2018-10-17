import operator

import pytest

from pyglyt.group import Group


@pytest.fixture
def trivial_group():
    return Group({0}, operator.add)


class TestGroup:
    def test_group_init(self, trivial_group):
        G = trivial_group
        assert set(G.generators) == {0}
        assert G.operation == operator.add
        assert G.identity is None

    def test_group_repr(self, trivial_group):
        actual = repr(trivial_group)
        expected = "Group(generators={0}, operation=<built-in function add>)"
        assert actual == expected

    def test_powers_of_1_in_Z2_are_1_and_0(self):
        def add_mod_2(x, y):
            return operator.add(x, y) % 2

        Z_2 = Group((1,), add_mod_2)
        powers = Z_2._powers(1)
        actual = tuple(powers)
        expected = (1, 0)
        assert actual == expected

    def test_first_5_powers_of_1_in_integers(self):
        Z = Group((1,), operator.add)
        powers = Z._powers(1, inverse=-1)
        actual = tuple(next(powers) for _ in range(5))
        expected = (0, 1, -1, 2, -2)
        assert actual == expected
