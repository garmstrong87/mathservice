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
app = Flask(__name__)

# List of functions with mapping in this service.
implemented_functions = ["fibonacci", "fibonacci_sum"]

@app.route("/function", methods=['GET'])
def list_implemented_functions():
    #
    # Return the list of functions implemented by the service 
    # as a JSON string.
    #
    return json.dumps({'functions': implemented_functions})


def create_json_error_message(error_cause):
    # Put together JSON error message
    return json.dumps({'called_url': request.url, 
                       'called_method': request.method, 
                       'error_message': error_cause.message()})

    
def get_fibonacci_series():  
    # Get the requested number of items in the series
    try:
        number_of_items = int(request.args.get('number', ''))
    except Exception:
        # Number not an integer, send error message
        raise MathServiceError.NonIntegerError("Number")
    
    # Get list of Fibonacci numbers
    try:
        return fibonacci.create_fibonacci_series(number_of_items)
    except MathServiceError.MathServiceError as error_cause:
        raise error_cause  # Send error up
        
    
@app.route('/function/fibonacci', methods=['GET'])
def calculate_fibonacci_series():
    # Find and return the first X number in the Fibonacci Series.  
    # With X being the input number_of_items.  The return is
    # currently formatted as a JSON document.   Number of items 
    # returned is bounded at MAX_FIBONACCI_NUMBERS
    # on the Fibonacci object.  Negative numbers not allowed. 
               
    # Get list of Fibonacci numbers
    try:
        series_object = get_fibonacci_series()
        series_list   = series_object.get_series()
    except MathServiceError.MathServiceError as error_cause:
        return create_json_error_message(error_cause)
        
    # Return as a properly formatted JSON object
    return json.dumps({'function' : 'fibonacci', 'list_size': len(series_list), 
                       'fibonacci_numbers': series_list})
    
    
@app.route('/function/fibonacci_sum', methods=['GET'])
def calculate_fibonacci_series_sum():
    # Find and return the sum of the first X number in the Fibonacci Series.  
    # With X being the input number_of_items.  The return is
    # currently formatted as a JSON document.   The number of items 
    # that can be summed is bounded at MAX_FIBONACCI_NUMBERS
    # on the Fibonacci object.  Negative numbers not allowed. 
               
        # Get list of Fibonacci numbers
    try:
        series_object = get_fibonacci_series()
    except MathServiceError.MathServiceError as error_cause:
        return create_json_error_message(error_cause)
    
    # Return as a properly formatted JSON object
    return json.dumps({'function' : 'fibonacci_sum', 
                       'sum': series_object.get_series_sum()})
    
    
    
if __name__ == "__main__":
    app.run()