class TreeException(Exception):
    '''
    The tree exception is a template exception class
    which raises an exception when the user input is not correct.
    '''
    def __init__(self, text) -> None:
        super().__init__(text)

    def __str__(self) -> str:
        return "Error: '{}'".format(self.args[0])
