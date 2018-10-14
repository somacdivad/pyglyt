import operator

import pytest

from pyglyt.group import Group


@pytest.fixture
def trivial_group():
    return Group({0}, operator.add)


class TestGroup:
    def test_group_init(self, trivial_group):
        G = trivial_group
        assert set(G.generators) == set()
        assert G.operation == operator.add
        assert G.identity is None

    def test_group_repr(self, trivial_group):
        actual = repr(trivial_group)
        expected = "Group(generators={0}, operation=<built-in function add>)"
        assert actual == expected
