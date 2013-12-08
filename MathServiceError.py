#  MathServiceError - For storing service and passing error information within
#                         the mathservice.
#


class MathServiceError():
        
    def __init__( self, error_message ):
        # Init method.
        self.error_message = error_message;
        
        
    def message( self ):
        # Return error message.
        return self.error_message