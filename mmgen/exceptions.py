class InputConstraintException(Exception):
    """
    Raised when a configured constraint makes it impossible to generate a mystery
    """
    def __init__(self, message):
        super(InputConstraintException, self).__init__(message)
