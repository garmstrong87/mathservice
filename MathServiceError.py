#  MathServiceError - For storing service and passing error information within
#                         the mathservice.
#


class MathServiceError():
    # Base class for errors in the MathService    
    error_message = None
    message_type  = "Default Math Service Error"
        
    def __init__(self, error_message=None):
        # Init method - initialize to input if any
        self.error_message = error_message;
        
    def message(self):
        # Return error message.
        return self.error_message
        
    def type(self):
        # Return message type
        return self.type
        
        
class NoInputError(MathServiceError):
    # Indicates that a negative index was selected in a list or series.
    message_type  = "Default NoInputError Error"
        
        
class ParameterError(MathServiceError):
    # Indicates that a negative index was selected in a list or series.
    dummy_message = "Error with parameter %s."
    message_type  = "Default Parameter Error"
    
    def __init__(self, parameter=None):
        # Initialization method - initialize parameter if supplied
        if parameter:
            self.error_message = self.dummy_message % parameter
        else:
            # initialize to empty dummy message for information purposes.
            self.error_message = self.dummy_message


class NonIntegerError(ParameterError):
    # Indicates that a negative index was selected in a list or series.
    dummy_message = "%s must a non-negative integer."
    message_type  = "Non-Integer Parameter Error"


class NegativeIndiceError(ParameterError):
    # Indicates that a negative index was selected in a list or series.
    dummy_message = "%s must a non-negative integer."
    message_type  = "Need Non-Negative Parameter Error"


class OutOfRangeError(ParameterError):
    # Indicates that an index was selected in a list or series out of
    # the allowed range.
    dummy_message = "%(parameter)s cannot be greater than %(upper_bound)i."
    message_type  = "Parameter Out of Range Error"
    
    def __init__(self, parameter=None, upper_bound=None):
        # Initialization method - initialize upper bound if supplied
        if not parameter:
            # Insert dummy to let it continue and show parameter value missing
            parameter = "(parameter)"
            
        if not upper_bound:
            # upperbound not provided give -1 to show no input
            self.error_message = self.dummy_message % {'parameter': parameter,
                                                     'upper_bound': -1}
        else:
            # initialize to empty dummy message for information purposes.
            self.error_message = self.dummy_message % {'parameter': parameter,
                                                  'upper_bound': upper_bound}


    