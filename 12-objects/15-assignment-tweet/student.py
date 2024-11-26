class Tweet:
    def __init__(self, message: str, max_length: int):
        if max_length < 1:
            raise ValueError("max_length must be at least 1.")
        self._max_length = max_length
        self._message = self.__truncate_message(message)

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, new_message: str):
        self._message = self.__truncate_message(new_message)

    @property
    def max_length(self):
        return self._max_length

    @max_length.setter
    def max_length(self, new_max_length: int):
        if new_max_length < 1:
            raise ValueError("max_length must be at least 1.")
        self._max_length = new_max_length
        self._message = self.__truncate_message(self._message)

    def __truncate_message(self, message: str):
        return message[:self._max_length]
