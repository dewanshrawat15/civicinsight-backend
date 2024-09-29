from rest_framework.exceptions import APIException

class ServiceUnavailableException(APIException):
    status_code = 503
    default_code = 'service_unavailable'
    default_detail = "It seems we're experiencing unusually high traffic, please try again later."
    
class UnauthorisedException(APIException):
    status_code = 401
    default_code = 'unauthorised'
    default_detail = 'User unauthorised, please try again.'