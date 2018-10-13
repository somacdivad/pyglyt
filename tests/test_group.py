import operator

import pytest

from pyglyt.group import Group


@pytest.fixture
def trivial_group():
    return Group()


@pytest.fixture(scope="module", params=[0, 0.0])
def non_iterable(request):
    return request.param


@pytest.fixture(scope="module", params=[0, 0.0, "", [], {}, set()])
def non_callable(request):
    return request.param


class TestGroup:
    def test_group_init(self, trivial_group):
        G = trivial_group
        assert set(G.generators) == set()
        assert G.identity is 0
        assert G.operation == operator.add

    def test_group_repr(self, trivial_group):
        actual = repr(trivial_group)
        expected = "Group<generators=set(), operation=<built-in function add>, identity=0>"
        assert actual == expected
