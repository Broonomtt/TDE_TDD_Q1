import pytest
from calc import soma

@pytest.mark.parametrize('a,b,resultado', [(0, 0, 0), (-2,-5,-7), (-2, 5,3), (7.5, 5.4,12.9), (-1.0, -2.0,-3.0)])
def test_soma(a,b, resultado):
    assert soma(a,b) == resultado
