# fibonacci.py - Provide Fibonacci Utilities.  
#
# Calculate Fibonacci Series [ 0, 1, 1, f(n-2) + f(n-1), .... ]
# 

import MathServiceError

# Define maximum number of numbers that will be calculated in the series.
MAX_FIBONACCI_NUMBERS = 1000

class fibonacci_series(object):

    def __init__(self, number_of_items=None):
        # 
        # Calculate the Fibonacci Series up to number_of_items terms. 
        #
        
        # Check if input is empty
        if number_of_items is None:
            raise MathServiceError.NoInputError("No input to define number"
                                                " of terms")
    
        # Check if input is an integer or long
        if not isinstance(number_of_items, (int, long)):
            raise MathServiceError.NonIntegerError("Number")
          
        # Check if greater than maximum terms allowed
        if number_of_items > MAX_FIBONACCI_NUMBERS:
            raise MathServiceError.OutOfRangeError("Number", 
                                                   MAX_FIBONACCI_NUMBERS)
                                    
        # Check if number negative
        if number_of_items < 0:
            raise MathServiceError.NegativeIndiceError("Number")
       
        # Special case 0 returns empty list
        self.series = []
        if number_of_items == 0:
            return
        
        # Special case first number
        self.series.append(0)
        if number_of_items == 1:
            return 
            
        # Special case second number
        self.series.append(1)
        if number_of_items == 2:
            return 
            
        # Cases for the rest of the terms in the series.
        count = 3
        while count <= number_of_items:
            # list starts at 0 so instead of list[ n - 2 ] + list[ n - 1 ]
            # it needs to be shifted back 1 to list[ n - 3 ] + list[ n - 2 ]
            self.series.append(self.series[count - 3] + self.series[count - 2])
            count = count + 1
            
    def get_series(self):
        # Return the entire series
        return self.series
        
        
    def get_series_term(self, index):
        # Return the the term (index) from the series
        # First term is 1 and so on
        
        if index < 1 or index > len(self.series):
            raise MathServiceError.OutOfRangeError("index", 
                                                   len(self.series))
        
        return self.series[index - 1]

    def get_series_last_term(self):
        # Return the the term (index) from the series
        # First term is 1 and so on
        
        if len(self.series) == 0:  # No term to return
            raise MathServiceError.OutOfRangeError("index", 
                                                   len(self.series))
        
        return self.series[len(self.series) - 1]

        
    def get_series_sum(self):
        # Return the sum for entire series
        series_sum = 0
        count = 0
        while count < len(self.series):
            series_sum = series_sum + self.series[count]
            count = count + 1
            
        return series_sum
        
        
def create_fibonacci_series(number=None):
    # Method to return populated fibonacci series object
    return fibonacci_series(number)