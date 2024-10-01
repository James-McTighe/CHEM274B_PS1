import sys

sys.path.append('/home/james_mctighe/chem_274B/problem_sets/CHEM274B_PS1/pset1_starter_code/')

from valid_symbols import Solution

def test_valid_symbols():
    testClass = Solution

    assert testClass.valid_symbols(testClass,'()')
    assert testClass.valid_symbols(testClass,'[]')
    assert testClass.valid_symbols(testClass,'{([])}')
    assert not testClass.valid_symbols(testClass,'(()]]')