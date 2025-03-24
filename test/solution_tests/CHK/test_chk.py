from solutions.CHK import checkout_solution
import pytest


class TestCHK():
    def test_chk(self):
        assert checkout_solution.checkout("A,B,C,D") == 115
        assert checkout_solution.checkout("A,A,A") == 130
        assert checkout_solution.checkout("B,B") == 45
        assert checkout_solution.checkout("A,A,A,A") == 180
        assert checkout_solution.checkout("E") == -1



    # def test_sum_error(self):
    #     with pytest.raises(ValueError, match="Input is out of range"):
    #         sum_solution.compute(-1,-2)
        
    #     with pytest.raises(ValueError, match="Input is out of range"):
    #         sum_solution.compute(101,2)

