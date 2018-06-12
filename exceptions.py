# Exception try, except or else and finally
n = 0
try:
    x = int(100 / n)
# We can set specific exceptions here like.
# ZeroDivisionError, NameError and TypeError etc.
except Exception as ex:
    print('Exception {0}'.format(ex))
else:
    print('Result of {dividend}/{divisor} = {quotient}'.format(
        dividend=100, divisor=n, quotient=x))
finally:
    print('Final clause')


# User-defined Exceptions
class UDException(Exception):
    """User defined exception."""
    def __init__(self, message):
        self.message = message

try:
    raise UDException('User-defined Exceptions')
except UDException as ex:
    print('Exception', ex.message)
