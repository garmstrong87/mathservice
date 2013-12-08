mathservice
===========

Example RESTful Web service providing Fibonacci Series information

This project is a simple web service example.  The web service is to provide
specialized mathematical processing upon request.  The example provides results
of the Fibonacci Series based upon a numeric input with a JSON response.  
Expansion for future additional mathematical processing functionality is 
accounted for. 

Files:

readme              - This file.
mathservice.py      - Sets up and runs Flask server, as well as, providing all
                      the web entry points.
fibonacci.py        - Provides Fibonacci Utilities.
MathServiceError.py - Captures error/exception information from within the service.
