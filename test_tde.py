import pytest
from calc import soma

@pytest.mark.parametrize('n1,n2,resultado', [(0, 0, 0), (-2,-5,-7), (-2, 5,3), (7.5, 5.4,12.9), (-1.0, -2.0,-3.0), ('DOIS', 2, None)])
def test_soma(n1, n2, resultado):
    assert soma(n1, n2) == resultado
