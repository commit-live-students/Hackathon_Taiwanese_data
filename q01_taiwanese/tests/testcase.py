import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal

original_return = pd.read_csv('Original_classes.csv',header=None)
student_return = pd.read_csv('../predicted_class.csv',header=None)


class Testing(unittest.TestCase):
	def test_return(self):
            assert_frame_equal(len(student_return), len(original_return), "Return value shape does not match expected value")

