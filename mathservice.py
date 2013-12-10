# mathservice.py - Sets up and runs Flask server.  
#
# Provides URL mappings and handles the calls for the function service. 
#

import json

import fibonacci 
import MathServiceError

from flask import Flask
from flask import request

# Web Server initialization
app = Flask( __name__ )

# List of functions with mapping in this service.
implemented_functions = [ "fibonacci" ]

@app.route( "/function", methods=[ 'GET' ] )
def list_implemented_functions():
    #
    # Return the list of functions implemented by the service 
    # as a JSON string.
    #
    return json.dumps( { 'functions': implemented_functions } )


def create_json_error_message( error_cause ):
    # Put together JSON error message
    return json.dumps( { 'called_url': request.url, 
                         'called_method': request.method, 
                         'error_message': error_cause.message() } )

    
@app.route( '/function/fibonacci', methods=[ 'GET' ] )
def calculate_fibonacci_series():
    # Find and return the first X number in the Fibonacci Series.  
    # With X being the input number_of_items.  The return is
    # currently formatted as a JSON document.   Number of items 
    # returned is bounded at MAX_FIBONACCI_NUMBERS
    # on the Fibonacci object.  Negative numbers not allowed. 
               
    # Get the requested number of items in the series
    try:
        number_of_items = int( request.args.get( 'number', '' ) )
    except Exception:
        # Number not an integer, send error message
        return create_json_error_message( MathServiceError.NonIntegerError( "Number" ) )
    
    # Get list of Fibonacci numbers
    try:
        series_list = fibonacci.get_fibonacci_series( number_of_items )
    except MathServiceError.MathServiceError as error_cause:
        return create_json_error_message( error_cause )
    
    # Check that proper number of items in the series returned
    if len( series_list ) < number_of_items:
        return create_json_error_message( "Server did not return proper number of items from the series."  )
    
    # Return as a properly formatted JSON object
    return json.dumps( { 'function' : 'fibonacci', 'list_size': len( series_list ), 
                         'fibonacci_numbers': series_list } )
    
    
    
if __name__ == "__main__":
    app.run()