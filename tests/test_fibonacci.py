#
# test_fibonacci.py - Perform unit tests to validate Fibonacci calculations 
#                     and ability to handle error conditions.
#  

import unittest

import fibonacci
import MathServiceError

class TestFibonacciCreate(unittest.TestCase):
    # Test the creation of the series and validate the correctness 
    # of the creation

    def test_fibonacci_with_negative_input(self):
        # Assure negative input for number of terms raises proper error
        with self.assertRaises(MathServiceError.NegativeIndiceError):
           fibonacci.create_fibonacci_series(-5)

           
    def test_fibonacci_with_no_input(self):
        # Assure negative input for number of terms raises proper error
        with self.assertRaises(MathServiceError.NoInputError):
           fibonacci.create_fibonacci_series()

           
    def test_fibonacci_with_input_above_max(self):
        # Assure input with a value larger than MAX_FIBONACCI_NUMBERS raises 
        # proper error
        with self.assertRaises(MathServiceError.OutOfRangeError):
           fibonacci.create_fibonacci_series(fibonacci.MAX_FIBONACCI_NUMBERS + 1)

           
    def test_fibonacci_with_non_int_input(self):
        # Assure non-integer input raises proper error 
        with self.assertRaises(MathServiceError.NonIntegerError):
           fibonacci.create_fibonacci_series("test")
           
           
    def test_fibonacci_zero_case(self):
        # Assure that request for 0 terms gives empty set.
        series = fibonacci.create_fibonacci_series(0)
        self.assertEqual( series.get_series(), [])
           
           
    def test_fibonacci_one_case(self):
        # Assure that request for 1 terms gives the proper set.
        series = fibonacci.create_fibonacci_series(1)
        self.assertEqual(series.get_series(), [0])
           
           
    def test_fibonacci_two_case(self):
        # Assure that request for 2 terms gives the proper set.
        series = fibonacci.create_fibonacci_series(2)
        self.assertEqual(series.get_series(), [0, 1])
           
           
    def test_fibonacci_three_case(self):
        # Assure that request for 3 terms gives the proper set.
        series = fibonacci.create_fibonacci_series(3)
        self.assertEqual(series.get_series(), [0, 1, 1])
    
    
    def test_fibonacci_ten_case(self):
        # Assure that request for 10 terms gives the proper set.
        series = fibonacci.create_fibonacci_series(10)
        self.assertEqual(series.get_series(), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        
        
    def test_fibonacci_proper_number_of_elements(self):
        # A validate proper number of terms for all possible sequences.
        for count in range(0, fibonacci.MAX_FIBONACCI_NUMBERS): 
            series = fibonacci.create_fibonacci_series(count)        
            self.assertEqual(len(series.get_series()), count)

            
class TestFibonacciFunctions(unittest.TestCase):
    # Test the functions of the object (except get_series tested with create)

    def setUp(self):
        self.zero = fibonacci.create_fibonacci_series(0)
        self.one  = fibonacci.create_fibonacci_series(1)
        self.two  = fibonacci.create_fibonacci_series(2)
        self.five = fibonacci.create_fibonacci_series(5)
        self.ten  = fibonacci.create_fibonacci_series(10)
        
    def test_fibonacci_sum(self):
        # Assure sum is correct for the series
        self.assertEqual(self.zero.get_series_sum(), 0)
        self.assertEqual(self.one.get_series_sum(), 0)
        self.assertEqual(self.two.get_series_sum(), 1)
        self.assertEqual(self.five.get_series_sum(), 7)
        self.assertEqual(self.ten.get_series_sum(), 88) 

    def test_fibonacci_get_term(self):
        # Assure get term function returns proper term or Out of bounds error.
        
        # no terms in zero
        with self.assertRaises(MathServiceError.OutOfRangeError):
           self.zero.get_series_term(-1)  # Should be out of bounds for all

        with self.assertRaises(MathServiceError.OutOfRangeError):
           self.zero.get_series_term(0)  # Should be out of bounds for all
        
        with self.assertRaises(MathServiceError.OutOfRangeError):
           self.zero.get_series_term(1)  # Past bounds

        # one term in one
        with self.assertRaises(MathServiceError.OutOfRangeError):
           self.one.get_series_term(-1)  # Should be out of bounds for all

        with self.assertRaises(MathServiceError.OutOfRangeError):
           self.one.get_series_term(0)  # Should be out of bounds for all
 
        self.assertEqual(self.one.get_series_term(1), 0)
         
        with self.assertRaises(MathServiceError.OutOfRangeError):
           self.one.get_series_term(2)  # past bounds
           
        # ten terms
        with self.assertRaises(MathServiceError.OutOfRangeError):
           self.ten.get_series_term(-1)  # Should be out of bounds for all

        with self.assertRaises(MathServiceError.OutOfRangeError):
           self.ten.get_series_term(0)  # Should be out of bounds for all
 
        valid_series = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for count in range(1, 10):  # Index for series starts at 1 then goes to length
            self.assertEqual(self.ten.get_series_term(count), valid_series[count - 1])
         
        with self.assertRaises(MathServiceError.OutOfRangeError):
           self.ten.get_series_term(11)  # past bounds
           
    def test_fibonacci_get_last_term(self):
        # Assure get the last term properly.
        
        # no terms in zero
        with self.assertRaises(MathServiceError.OutOfRangeError):
           self.zero.get_series_last_term()  # Should be out of bounds for all
 
        self.assertEqual(self.one.get_series_last_term(), 0)
        self.assertEqual(self.two.get_series_last_term(), 1)
        self.assertEqual(self.five.get_series_last_term(), 3)
        self.assertEqual(self.ten.get_series_last_term(), 34) 
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase( TestFibonacciFunctions )
    unittest.TextTestRunner( verbosity = 2 ).run( suite )
    suite = unittest.TestLoader().loadTestsFromTestCase( TestFibonacciCreate )
    unittest.TextTestRunner( verbosity = 2 ).run( suite )