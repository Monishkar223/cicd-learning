import pytest
from src.calculator import Calculator


class Test:
    def test_smoke_add(self):
        calc=Calculator()
        assert calc.add(1,2,3)==6

    def test_smoke_sub(self):
        calc=Calculator()
        assert calc.sub(10,4,2)==4

    def test_smoke_mul(self):
        calc=Calculator()
        assert calc.mul(1,2,3)==6
    
    def test_smoke_validation_empty(self):
        calc=Calculator()
    
        with pytest.raises(ValueError):
            calc.add()
        
        with pytest.raises(ValueError):
            calc.sub()
        
        with pytest.raises(ValueError):
            calc.mul()
    
    def test_smoke_validation_non_numeric(self):
    
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.add(1, "x", 3)
        with pytest.raises(TypeError):
            calc.sub(1, "x", 3)
        with pytest.raises(TypeError):
            calc.mul(1, "x", 3)
    

        