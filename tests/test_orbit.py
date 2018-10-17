from unittest import mock
import operator

from pyglyt.group import Group, Orbit
import pytest


@pytest.fixture(scope="module")
def integers_mod_2():
    def add_mod_2(x, y):
        return operator.add(x, y) % 2

    return Group((1,), add_mod_2)


@pytest.fixture(scope="module")
def orbit_of_1_in_Z2():
    def add_mod_2(x, y):
        return operator.add(x, y) % 2

    G = Group((1,), add_mod_2)
    return Orbit(G, 1, G.operation)


class TestOrbit:
    def test_orbit_init(self):
        G = Group((0,), operator.add)
        orbit = Orbit(G, 0, G.operation)
        assert orbit.group == G
        assert orbit.element == 0
        assert orbit.action == G.operation

    def test_orbit_no_cache(self):
        G = Group((0,), operator.add)
        orbit = Orbit(G, 0, G.operation, cache=False)
        set(orbit)
        actual = orbit._elements
        expected = []
        assert actual == expected

    def test_orbit_cache_exists(self, orbit_of_1_in_Z2):
        orbit = orbit_of_1_in_Z2
        set(orbit)
        assert set(orbit._elements) == {0, 1}

    def test_orbit_cache_used(self, orbit_of_1_in_Z2):
        elements = mock.PropertyMock(return_value={0, 1})
        _Orbit = mock.MagicMock(wraps=Orbit, return_value=orbit_of_1_in_Z2)
        orbit = _Orbit()
        orbit._elements = elements()
        set(orbit)
        elements.assert_called_with()

    def test_orbit_of_1_in_Z2_is_all_of_Z2(self, integers_mod_2):
        orbit = Orbit(integers_mod_2, 1, integers_mod_2.operation)
        actual = set(orbit)
        expected = {0, 1}
        assert actual == expected
