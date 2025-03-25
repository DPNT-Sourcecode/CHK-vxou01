from solutions.CHK import checkout_solution
import pytest


class TestCHK():
    def test_chk(self):
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 853
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("BB") == 45            
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAA") == 380
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("BEBEEE") == 160
        assert checkout_solution.checkout("ABCDEABCDE") == 280
        assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("HHHHH") == 45
        assert checkout_solution.checkout("HHHHHHHHHH") == 80
        assert checkout_solution.checkout("HHHHHHHHHHHHHHH") == 125
        assert checkout_solution.checkout("HHHHHHHHHHHH") == 100
        assert checkout_solution.checkout("K") == 70
        assert checkout_solution.checkout("KK") == 120
        assert checkout_solution.checkout("KKK") == 190
        assert checkout_solution.checkout("NNNM") == 120
        assert checkout_solution.checkout("NNNMM") == 135
        assert checkout_solution.checkout("NNNNNNMM") == 240
        assert checkout_solution.checkout("PPPP") == 200
        assert checkout_solution.checkout("PPPP") == 200
        assert checkout_solution.checkout("RRRQ") == 150
        assert checkout_solution.checkout("RRR") == 150
        assert checkout_solution.checkout("RRRRRRQ") == 300
        assert checkout_solution.checkout("RRRRRRQQ") == 300
        assert checkout_solution.checkout("RRRRRRQQQ") == 330
        assert checkout_solution.checkout("UUU") == 120
        assert checkout_solution.checkout("UU") == 80
        assert checkout_solution.checkout("VVV") == 130
        assert checkout_solution.checkout("VV") == 90
        assert checkout_solution.checkout("VVVVV") == 220
        assert checkout_solution.checkout("QQQ") == 80
        assert checkout_solution.checkout("QQQQ") == 110







    # def test_sum_error(self):
    #     with pytest.raises(ValueError, match="Input is out of range"):
    #         sum_solution.compute(-1,-2)
        
    #     with pytest.raises(ValueError, match="Input is out of range"):
    #         sum_solution.compute(101,2)


