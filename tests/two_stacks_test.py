import sys

sys.path.append('/home/james_mctighe/chem_274B/problem_sets/CHEM274B_PS1/pset1_starter_code/')

from queue_two_stacks import Queue

def test_enqueue():
    q = Queue()
    # q.stack1 = []
    # q.stack2 = []
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    

    assert not q.is_empty()
    assert q.peek() == 1