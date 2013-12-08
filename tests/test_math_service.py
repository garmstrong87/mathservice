#
# test_function_service.py - Perform unit tests to validate mappings and responses for the service.
#  

import unittest
import json

from flask import Flask

from mathservice import * 

from MathServiceError import MathServiceError

class TestServiceFunctions( unittest.TestCase ):

    def test_list_of_implemented_functions( self ):
        # Assure that the proper JSON message type comes back
        response = json.loads( list_implemented_functions() )
        self.assertTrue( 'functions' in response )
        
        # Only one current implemented function
        self.assertEqual( len( response[ 'functions' ] ), 1 )

        
    def test_fibonacci_valid_response( self ):
        # Verify proper format of JSON response
        app = Flask( __name__ )

        with app.test_request_context( '/function/fibonacci?number=3' ):
            response = json.loads( calculate_fibonacci_series() )
            self.assertTrue( 'function' in response )
            self.assertEqual( response[ 'function' ], 'fibonacci' )
            self.assertTrue( 'list_size' in response )
            self.assertTrue( 'fibonacci_numbers' in response )
            self.assertEqual( len( response[ 'fibonacci_numbers' ] ), 3 )                   


    def test_fibonacci_invalid_response( self ):
        # Verify proper format of JSON response for error message
        app = Flask( __name__ )
        app.config['TESTING'] = True

        with app.test_request_context( '/function/fibonacci?number=-3' ):
            response = json.loads( calculate_fibonacci_series() )
            self.assertTrue( 'called_url' in response )
            self.assertTrue( 'called_method' in response )
            self.assertTrue( 'error_message' in response ) 
            
            
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase( TestSequenceFunctions )
    unittest.TextTestRunner( verbosity = 2 ).run( suite )