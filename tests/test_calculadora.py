import sys,os
#sys.path.insert(0, os.path.abspath('...'))


import examplepy.calculator as calc


def test_calculator():
    assert calc.suma(5,7) == 12
    assert calc.resta(12,7) == 5

