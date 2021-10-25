import examplepy.calculator as calc
import pytest
def test_calculator2():
    assert calc.multiplicacion(7,5) ==  35
    assert calc.division(35,7) == 5

    with pytest.raises(ValueError):
        assert calc.division(35,0)