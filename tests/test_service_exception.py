#
# test_service_exception.py - unit tests validating exception information.
#  

import unittest

from MathServiceError import MathServiceError

class TestExceptionFunctions( unittest.TestCase ):

    def setUp( self ):
        # Setup - Create standard message for test and create error with the message
        self.test_error_message = "Test Error Message"
        self.exception = MathServiceError( self.test_error_message )

    def test_message( self ):
        # Assure that the message contained and returned by the error matches the
        # message input.
        self.assertEqual( self.exception.message(), self.test_error_message )

            
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase( TestSequenceFunctions )
    unittest.TextTestRunner( verbosity = 2 ).run( suite )