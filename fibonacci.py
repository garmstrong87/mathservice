# fibonacci.py - Provide Fibonacci Utilities.  
#
# Calculate Fibonacci Series [ 0, 1, 1, f(n-2) + f(n-1), .... ]
# 

from MathServiceError import MathServiceError

# Define maximum number of numbers that will be calculated in the series.
MAX_FIBONACCI_NUMBERS = 1000

def get_fibonacci_series( number_of_items ):
    # 
    # Calculate the Fibonacci Series up to number_of_items terms. 
    #
    
    # Check if input is an integer or long
    if not isinstance( number_of_items, ( int, long ) ):
        raise MathServiceError( "Number of items requested must be an integer value." )
          
    # Check if greater than maximum terms allowed
    if number_of_items > MAX_FIBONACCI_NUMBERS:
        raise MathServiceError( "Number of items requested cannot be greater than " + 
                                str( MAX_FIBONACCI_NUMBERS ) )
                                    
    # Check if number negative
    if number_of_items < 0:    
        raise MathServiceError( "Number of items requested must a non-negative integer." )
       
    # Special case 0 returns empty list
    list_values = []
    if number_of_items == 0:
        return list_values
        
    # Special case first number
    list_values.append( 0 )
    if number_of_items == 1:
        return list_values
            
    # Special case second number
    list_values.append( 1 )
    if number_of_items == 2:
        return list_values
            
    # Cases for the rest of the terms in the series.
    count = 3
    while count <= number_of_items:
        # list starts at 0 so instead of list[ n - 2 ] + list[ n - 1 ]
        # it needs to be shifted back 1 to list[ n - 3 ] + list[ n - 2 ]
        list_values.append( list_values[ count - 3 ] + list_values[ count - 2 ] )
        count = count + 1
        
    return list_values
