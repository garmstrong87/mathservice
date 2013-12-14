#
# test_function_service.py - Perform unit tests to validate mappings and responses for the service.
#  

import unittest
import json

from flask import Flask

import mathservice
import MathServiceError

class TestServiceFunctions(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        
        
    def test_list_of_implemented_functions(self):
        # Assure that the proper JSON message type comes back
        response = json.loads(mathservice.list_implemented_functions())
        self.assertTrue('functions' in response)
        
        # Only one current implemented function
        self.assertEqual(len(response['functions']), 2)

        
    def test_fibonacci_series_valid_response(self):
        # Verify proper format of JSON response
        with self.app.test_request_context('/function/fibonacci?number=3'):
            response = json.loads(mathservice.calculate_fibonacci_series())
            self.assertTrue('function' in response)
            self.assertEqual(response['function'], 'fibonacci')
            self.assertTrue('list_size' in response)
            self.assertTrue('fibonacci_numbers' in response)
            self.assertEqual(len(response['fibonacci_numbers']), 3)                   

            
    def test_fibonacci_series_invalid_response( self ):
        # Verify proper format of JSON response for error message
        with self.app.test_request_context('/function/fibonacci?number=-3'):
            response = json.loads(mathservice.calculate_fibonacci_series())
            self.assertTrue('called_url' in response)
            self.assertTrue('called_method' in response)
            self.assertTrue('error_message' in response) 
            
            
    def test_fibonacci_series_sum_valid_response(self):
        # Verify proper format of JSON response
        with self.app.test_request_context('/function/fibonacci_sum?number=3'):
            response = json.loads(mathservice.calculate_fibonacci_series_sum())
            self.assertTrue('function' in response)
            self.assertEqual(response['function'], 'fibonacci_sum')
            self.assertTrue('sum' in response)
            self.assertEqual(response['sum'], 2)                   


    def test_fibonacci_series_sum_invalid_response(self):
        # Verify proper format of JSON response for error message
        with self.app.test_request_context('/function/fibonacci_sum?number=-3'):
            response = json.loads(mathservice.calculate_fibonacci_series_sum())
            self.assertTrue('called_url' in response)
            self.assertTrue('called_method' in response)
            self.assertTrue('error_message' in response) 
            
            
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestServiceFunctions)
    unittest.TextTestRunner(verbosity = 2).run(suite)