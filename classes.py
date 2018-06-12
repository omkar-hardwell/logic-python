# Class definition
class Demo:
    """This is demo class."""
    def __init__(self, message):
        self.message = message

    def get_message(self):
        return 'Hello {}!'.format(self.message)


obj = Demo('World')
print(obj.get_message())
