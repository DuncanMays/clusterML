class Base():
    def __init__(self, data=None):
        super().__init__()
        if data:
            self.__dict__ = data