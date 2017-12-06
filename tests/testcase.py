
import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
	def setUp(self):
	    self.path = '../notebook/predicted_class.csv'
	    self.student_return = pd.read_csv(self.path,header=None)
	    self.original_return = pd.read_csv('Original_classes.csv',header=None)	

	def test_return(self):
            assert_frame_equal(self.student_return, self.original_return, "Return value shape does not match expected value")
	
if __name__=='__main__':
    unittest.main()
