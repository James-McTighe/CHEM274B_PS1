import sys

sys.path.append('/home/james_mctighe/chem_274B/problem_sets/CHEM274B_PS1/pset1_starter_code/')

from bin_search import Solution

def test_bin_search():
    a = Solution()

    b = [x for x in range(1001)]

    assert a.binary_search(b,450) == 450
    assert a.binary_search(b,0) == 0
    assert a.binary_search(b,1000) == 1000