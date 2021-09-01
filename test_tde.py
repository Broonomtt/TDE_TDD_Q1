import pytest
from calc import soma

@pytest.mark.parametrize('a,b,expected', [(0, 0, 0)])
def test_soma(a,b, expected):
    assert soma(a,b) == expected
