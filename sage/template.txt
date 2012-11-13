import time
import unittest

class TP(unittest.TestCase):
    def test_xxx(self):
        #self.assertEqual(ds3(), N(3))

def solve():
	pass

testing = 0

def init(t):
    global testing
    testing = t
init(0)

if testing:
    unittest.main()
else:
    t = time.time()
    print "answer = %s" % solve()
    print "(%s)" % (time.time() - t)

