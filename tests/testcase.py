
import unittest
import pandas as pd

#path = 'Orginal_classes.csv'

class Testing(unittest.TestCase):
	def setUp(self):
	    self.path = '../notebook/predicted_class.csv'
	    self.student_return = pd.read_csv(self.path,header=None)
	    self.original_return = pd.read_csv('Orginal_classes.csv')	

	def test_return(self):
            self.assertEqual(self.student_return.shape, (6000, 1), "Return value shape does not match expected value")
	
if __name__=='__main__':
    unittest.main()
