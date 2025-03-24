from solutions.CHK import checkout
import pytest


class TestCHK():
    def test_chk(self):
        assert sum_solution.compute(1, 2) == 3

    # def test_sum_error(self):
    #     with pytest.raises(ValueError, match="Input is out of range"):
    #         sum_solution.compute(-1,-2)
        
    #     with pytest.raises(ValueError, match="Input is out of range"):
    #         sum_solution.compute(101,2)
