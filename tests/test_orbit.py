import operator

from pyglyt.group import Group, Orbit


class TestOrbit:
    def test_orbit_init(self):
        G = Group((0,), operator.add)
        orbit = Orbit(G, 0, G.operation)
        assert orbit.group == G
        assert orbit.element == 0
        assert orbit.action == G.operation

    def test_orbit_of_1_in_Z2_is_all_of_Z2(self):
        def add_mod_2(x, y):
            return operator.add(x, y) % 2

        Z_2 = Group((1,), add_mod_2)
        orbit = Orbit(Z_2, 1, Z_2.operation)
        actual = set(orbit)
        expected = {0, 1}
        assert actual == expected
