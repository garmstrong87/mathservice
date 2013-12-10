#  MathServiceError - For storing service and passing error information within
#                         the mathservice.
#


class MathServiceError():
    # Base class for errors in the MathService
    
    error_message = None
    message_type  = "Math Service Default"
        
    def __init__( self, error_message=None ):
        # Init method - initialize to input if any
        self.error_message = error_message;
        
    def message( self ):
        # Return error message.
        return self.error_message
        
    def type( self ):
        # Return message type
        return self.type
        
        
class ParameterError( MathServiceError ):
    # Indicates that a negative index was selected in a list or series.

    dummy_message = "Error with parameter %s."
    
    def __init__( self, parameter=None ):
        # Initialization method - initialize parameter if supplied
        if parameter:
            self.error_message = self.dummy_message % parameter
        else:
            # initialize to empty dummy message for information purposes.
            self.error_message = self.dummy_message


class NonIntegerError( ParameterError ):
    # Indicates that a negative index was selected in a list or series.

    dummy_message = "%s must a non-negative integer."


class NegativeIndiceError( ParameterError ):
    # Indicates that a negative index was selected in a list or series.

    dummy_message = "%s must a non-negative integer."


class OutOfRangeError( ParameterError ):
    # Indicates that an index was selected in a list or series out of
    # the allowed range.

    dummy_message = "%(parameter)s cannot be greater than %(upper_bound)i."
    
    def __init__( self, parameter=None, upper_bound=None ):
        # Initialization method - initialize upper bound if supplied
        if not parameter:
            # Insert dummy to let it continue and show parameter value missing
            parameter = "(parameter)"
            
        if not upper_bound:
            # Leave upperbound as %(upper_bound) but set parameter
            self.error_message = self.dummy_message % { 'parameter': parameter }
        else:
            # initialize to empty dummy message for information purposes.
            self.error_message = self.dummy_message % { 'parameter': parameter,
                                                  'upper_bound': upper_bound }


    