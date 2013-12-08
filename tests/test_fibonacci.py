#
# test_fibonacci.py - Perform unit tests to validate Fibonacci calculations and ability to handle error conditions.
#  

import unittest

import fibonacci
from MathServiceError import MathServiceError

class TestFibonacciFunctions( unittest.TestCase ):

    def test_fibonacci_with_negative_input( self ):
        # Assure negative input for number of terms raises proper error
        with self.assertRaises( MathServiceError ):
           fibonacci.get_fibonacci_series( -5 )

           
    def test_fibonacci_with_input_above_max( self ):
        # Assure input with a value larger than MAX_FIBONACCI_NUMBERS raises proper error
        with self.assertRaises( MathServiceError ):
           fibonacci.get_fibonacci_series( fibonacci.MAX_FIBONACCI_NUMBERS + 1 )

           
    def test_fibonacci_with_non_int_input( self ):
        # Assure non-integer input raises proper error 
        with self.assertRaises( MathServiceError ):
           fibonacci.get_fibonacci_series( "test" )
           
           
    def test_fibonacci_zero_case( self ):
        # Assure that request for 0 terms gives empty set.
        self.assertEqual( fibonacci.get_fibonacci_series( 0 ), [] )
           
           
    def test_fibonacci_one_case( self ):
        # Assure that request for 1 terms gives the proper set.
        self.assertEqual( fibonacci.get_fibonacci_series( 1 ), [ 0 ] )
           
           
    def test_fibonacci_two_case( self ):
        # Assure that request for 2 terms gives the proper set.
        self.assertEqual( fibonacci.get_fibonacci_series( 2 ), [ 0, 1 ] )
           
           
    def test_fibonacci_three_case( self ):
        # Assure that request for 3 terms gives the proper set.
        self.assertEqual( fibonacci.get_fibonacci_series( 3 ), [ 0, 1, 1 ] )
    
    
    def test_fibonacci_ten_case( self ):
        # Assure that request for 10 terms gives the proper set.
        self.assertEqual( fibonacci.get_fibonacci_series( 10 ), [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ] )
        
        
    def test_fibonacci_proper_number_of_elements( self ):
        # A validate proper number of terms for all possible sequences.
        for count in range( 0, fibonacci.MAX_FIBONACCI_NUMBERS ):        
            self.assertEqual( len( fibonacci.get_fibonacci_series( count ) ), count )
        
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase( TestSequenceFunctions )
    unittest.TextTestRunner( verbosity = 2 ).run( suite )