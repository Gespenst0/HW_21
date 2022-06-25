class StorageFull(Exception):
    def __init__(self, message='Capacity exceeded'):
        self.message = message
        super().__init__(message)


class ItemsNotFound(Exception):
    def __init__(self, message='Items not found'):
        self.message = message
        super().__init__(message)


class MessageError(Exception):
    def __init__(self, message='Incorrect message'):
        self.message = message
        super().__init__(message)
